const BASE_URL = 'http://127.0.0.1:8000/';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = async function() {
    const articleId = window.location.pathname.split('/').filter(Boolean).pop();

    try {
        const [articleResponse, commentsResponse] = await Promise.all([
            fetch(`${BASE_URL}api/articles/Camping/${articleId}/`),
            fetch(`${BASE_URL}api/articles/${articleId}/comments/`)
        ]);

        if (!articleResponse.ok) {
            throw new Error(`Failed to fetch article: ${articleResponse.statusText}`);
        }

        if (!commentsResponse.ok) {
            throw new Error(`Failed to fetch comments: ${commentsResponse.statusText}`);
        }

        const [article, comments] = await Promise.all([
            articleResponse.json(),
            commentsResponse.json()
        ]);

        renderArticleDetail(article);
        renderCommentsHTML(comments);
    } catch (error) {
        console.error('Error fetching data:', error);
    }

    const deleteButton = document.getElementById('deleteButton');
    if (deleteButton) {
        deleteButton.addEventListener('click', async () => {
            const confirmDelete = confirm('정말로 이 게시글을 삭제하시겠습니까?');
            if (confirmDelete) {
                try {
                    const csrftoken = getCookie('csrftoken');
                    const response = await fetch(`${BASE_URL}api/articles/Camping/${articleId}/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken,
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                        }
                    });

                    if (!response.ok) {
                        if (response.status === 403) {
                            alert('삭제 권한이 없습니다.');
                        } else {
                            throw new Error(`Failed to delete article: ${response.statusText}`);
                        }
                    } else {
                        window.location.href = '/api/articles/Camping/';
                    }

                } catch (error) {
                    console.error('Error deleting article:', error);
                    alert('게시글 삭제 중 오류가 발생했습니다. 다시 시도해주세요.');
                }
            }
        });
    } else {
        console.error('Delete button not found');
    }

    const editButton = document.getElementById('editButton');
    if (editButton) {
        editButton.addEventListener('click', () => {
            const articleTitle = document.getElementById('article-title').innerText.replace('제목: ', '');
            const articleContent = document.getElementById('article-content').innerText.replace('내용: ', '');

            document.getElementById('edit-title').value = articleTitle;
            document.getElementById('edit-content').value = articleContent;

            document.getElementById('edit-article-modal').style.display = 'block';
        });
    }

    const saveEditButton = document.getElementById('saveEditButton');
    if (saveEditButton) {
        saveEditButton.addEventListener('click', async () => {
            const updatedTitle = document.getElementById('edit-title').value;
            const updatedContent = document.getElementById('edit-content').value;

            try {
                const csrftoken = getCookie('csrftoken');
                const response = await fetch(`${BASE_URL}api/articles/Camping/${articleId}/`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken,
                        'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                    },
                    body: JSON.stringify({
                        title: updatedTitle,
                        content: updatedContent
                    })
                });

                if (!response.ok) {
                    throw new Error(`Failed to update article: ${response.statusText}`);
                }

                const updatedArticle = await response.json();
                document.getElementById('article-title').innerText = '제목: ' + updatedArticle.title;
                document.getElementById('article-content').innerText = '내용: ' + updatedArticle.content;

                document.getElementById('edit-article-modal').style.display = 'none';

            } catch (error) {
                console.error('Error updating article:', error);
                alert('게시글 수정 중 오류가 발생했습니다. 다시 시도해주세요.');
            }
        });
    }

    document.getElementById('submitCommentButton').addEventListener('click', async function() {
        const commentContent = document.getElementById('new-comment').value;
        if (commentContent.trim() === "") {
            alert("댓글을 입력하세요.");
            return;
        }

        try {
            const csrftoken = getCookie('csrftoken');
            const response = await fetch(`${BASE_URL}api/articles/${articleId}/comments/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                },
                body: JSON.stringify({ content: commentContent })
            });

            if (!response.ok) {
                throw new Error(`Failed to post comment: ${response.statusText}`);
            }

            const newComment = await response.json();
            document.getElementById('commentList').innerHTML += `
                <li data-comment-id="${newComment.id}">
                    <div class="comment-content">
                        <p>${newComment.content}</p>
                    </div>
                    <div class="comment-details">
                        <p>작성자: ${newComment.user.username}</p>
                        <p>작성일자: ${newComment.created_at}</p>
                    </div>
                    <div>
                        <button class="comment-button edit-comment-button">수정</button>
                        <button class="comment-button delete-comment-button">삭제</button>
                    </div>
                </li>
            `;

            document.getElementById('new-comment').value = '';

        } catch (error) {
            console.error('Error posting comment:', error);
            alert('댓글 작성 중 오류가 발생했습니다. 다시 시도해주세요.');
        }
    });

    document.addEventListener('click', async function(event) {
        if (event.target.classList.contains('delete-comment-button')) {
            const commentLi = event.target.closest('li');
            if (commentLi) {
                const commentId = commentLi.dataset.commentId || window.location.pathname.split('/').filter(Boolean).pop();
                if (!commentId) {
                    console.error('Error: commentId is missing or empty.');
                    return;
                }
                console.log('Deleting comment with ID:', commentId);  // Debugging
    
                try {
                    const csrftoken = getCookie('csrftoken');
                    const response = await fetch(`${BASE_URL}api/articles/comments/${commentId}/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken,
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                        }
                    });
    
                    if (!response.ok) {
                        throw new Error(`Failed to delete comment: ${response.statusText}`);
                    }
    
                    commentLi.remove();
    
                } catch (error) {
                    console.error('Error deleting comment:', error);
                    alert('댓글 삭제 중 오류가 발생했습니다. 다시 시도해주세요.');
                }
            } else {
                console.error('No parent <li> element found.');
            }
        }
    
        if (event.target.classList.contains('edit-comment-button')) {
            const commentLi = event.target.closest('li');
            if (commentLi) {
                const commentId = commentLi.dataset.commentId || window.location.pathname.split('/').filter(Boolean).pop();
                if (!commentId) {
                    console.error('Error: commentId is missing or empty.');
                    return;
                }
                const commentContent = commentLi.querySelector('.comment-content p').innerText;
    
                console.log('Editing comment with ID:', commentId);  // Debugging
    
                document.getElementById('edit-comment-content').value = commentContent;
                document.getElementById('saveCommentEditButton').dataset.commentId = commentId;
                document.getElementById('edit-comment-modal').style.display = 'block';
            } else {
                console.error('No parent <li> element found.');
            }
        }
    });
    
    document.getElementById('saveCommentEditButton').addEventListener('click', async function() {
        const commentId = this.dataset.commentId || window.location.pathname.split('/').filter(Boolean).pop();
        if (!commentId) {
            console.error('Error: commentId is missing or empty.');
            return;
        }
        const updatedContent = document.getElementById('edit-comment-content').value;
    
        console.log('Saving edit for comment ID:', commentId);  // Debugging
    
        try {
            const csrftoken = getCookie('csrftoken');
            const response = await fetch(`${BASE_URL}api/articles/comments/${commentId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token')
                },
                body: JSON.stringify({ content: updatedContent })
            });
    
            if (!response.ok) {
                const errorText = await response.text();
                console.error('Error response:', errorText);
                throw new Error(`Failed to update comment: ${response.statusText}`);
            }
    
            const updatedComment = await response.json();
            const commentElement = document.querySelector(`li[data-comment-id='${commentId}'] .comment-content p`);
            commentElement.innerText = updatedComment.content;
    
            document.getElementById('edit-comment-modal').style.display = 'none';
    
        } catch (error) {
            console.error('Error updating comment:', error);
            alert('댓글 수정 중 오류가 발생했습니다. 다시 시도해주세요.');
        }
    });
}   