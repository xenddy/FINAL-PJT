const BASE_URL = "http://127.0.0.1:8000/";

async function fetchTravelDetail() {
    const articleId = window.location.pathname.split('/').pop();
    const response = await fetch(`${BASE_URL}api/articles/Camping/${articleId}/`);
    const data = await response.json();
    renderArticleDetail(data);
}

function renderArticleDetail(article) {
    document.getElementById("article-title").innerText = article.title;
    document.getElementById("article-content").innerText = article.content;
    document.getElementById("article-author").innerText = article.author;
    document.getElementById("article-created-at").innerText = article.created_at;
}

function goBack() {
    window.history.back();
}

window.onload = function() {
    fetchTravelDetail();
    updateCommentList();
}

function updateCommentList() {
    const commentList = document.getElementById("commentList");
    commentList.innerHTML = "";

    const xhr = new XMLHttpRequest();
    xhr.open("GET", `${BASE_URL}api/articles/Camping/${articleId}/comments/`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const comments = JSON.parse(xhr.responseText);
                comments.forEach(function(comment) {
                    const li = document.createElement("li");
                    li.textContent = comment.content + " - " + comment.user;
                    commentList.appendChild(li);
                });
            } else {
                console.error("Error:", xhr.responseText);
            }
        }
    };
    xhr.send();
}

document.getElementById("commentForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const content = document.getElementById("commentContent").value;
    const xhr = new XMLHttpRequest();
    xhr.open("POST", `${BASE_URL}api/articles/Camping/${articleId}/comments/`, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 201) {
                updateCommentList();
            } else {
                console.error("Error:", xhr.responseText);
            }
        }
    };
    const data = JSON.stringify({"content": content});
    xhr.send(data);
});

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
