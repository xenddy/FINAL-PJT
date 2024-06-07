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

window.onload = fetchArticleDetail;

async function fetchArticleDetail() {
    const articleId = window.location.pathname.split('/').pop();
    
    try {
        const [articleResponse, commentsResponse] = await Promise.all([
            fetch(`${BASE_URL}api/articles/${articleId}/`),
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
        renderCommentsHTML(comments); // 댓글을 HTML로 렌더링
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function renderArticleDetail(article) {
    document.getElementById("article-title").innerText = article.title;
    document.getElementById("article-content").innerText = article.content;
    document.getElementById("article-author").innerText = article.author;
    document.getElementById("article-created-at").innerText = article.created_at;

    const deleteButton = document.getElementById('deleteButton');
    deleteButton.addEventListener('click', async () => {
        const confirmDelete = confirm('정말로 이 게시글을 삭제하시겠습니까?');
        if (confirmDelete) {
            try {
                const response = await fetch(`${BASE_URL}api/articles/Camping/${article.id}/`, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });
                
                if (!response.ok) {
                    throw new Error(`Failed to delete article: ${response.statusText}`);
                }

                // 삭제 후 캠핑 리스트 페이지로 이동
                window.location.href = '/api/articles/Camping/';

            } catch (error) {
                console.error('Error deleting article:', error);
            }
        }
    });
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
