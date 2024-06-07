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
    const articleId = window.location.pathname.split('/').filter(Boolean).pop(); // URL에서 article ID 추출

    try {
        const [articleResponse, commentsResponse] = await Promise.all([
            fetch(`${BASE_URL}api/articles/Leisure/${articleId}/`),
            fetch(`${BASE_URL}api/articles/Leisure/${articleId}/comments/`)
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
        renderCommentsHTML(comments); // 댓글을 HTML로 렌더링
    } catch (error) {
        console.error('Error fetching data:', error);
    }

    const deleteButton = document.getElementById('deleteButton');
    if (deleteButton) {
        deleteButton.addEventListener('click', async () => {
            const confirmDelete = confirm('정말로 이 게시글을 삭제하시겠습니까?');
            if (confirmDelete) {
                try {
                    const csrftoken = getCookie('csrftoken'); // CSRF 토큰 가져오기
                    const response = await fetch(`${BASE_URL}api/articles/Leisure/${articleId}/`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrftoken,
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token') // JWT 토큰 포함
                        }
                    });

                    if (!response.ok) {
                        if (response.status === 403) {
                            alert('삭제 권한이 없습니다.');
                        } else {
                            throw new Error(`Failed to delete article: ${response.statusText}`);
                        }
                    } else {
                        // 삭제 후 캠핑 리스트 페이지로 이동
                        window.location.href = '/api/articles/Leisure/';
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
                const response = await fetch(`${BASE_URL}api/articles/Leisure/${articleId}/`, {
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
                alert('게시글 수정 권한이 없습니다.');
            }
        });
    }
};

function renderArticleDetail(article) {
    document.getElementById("article-title").innerText = '제목: ' + article.title;
    document.getElementById("article-content").innerText = '내용: ' + article.content;
    document.getElementById("article-author").innerText = article.author;
    document.getElementById("article-created-at").innerText = article.created_at;
}

function renderCommentsHTML(comments) {
    const commentList = document.getElementById("commentList");
    commentList.innerHTML = "";

    if (comments.length > 0) {
        comments.forEach(comment => {
            commentList.innerHTML += renderCommentHTML(comment);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = "댓글이 없습니다.";
        commentList.appendChild(li);
    }
}

// Comment 데이터를 HTML로 변환하는 함수
function renderCommentHTML(comment) {
    return `
        <li>
            <p>${comment.content}</p>
            <p>작성자: ${comment.user.username}</p>
            <p>작성일자: ${comment.created_at}</p>
        </li>
    `;
}
