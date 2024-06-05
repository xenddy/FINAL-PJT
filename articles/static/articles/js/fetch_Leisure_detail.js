const BASE_URL = "http://127.0.0.1:8000/";

async function fetchTravelDetail() {
    // 현재 페이지의 URL 경로에서 게시물의 ID를 추출
    const articleId = window.location.pathname.split('/').pop();
    const response = await fetch(`${BASE_URL}api/articles/Leisure/${articleId}/`);
    const data = await response.json();
    console.log(data); // 받은 데이터를 콘솔에 출력하여 확인
    renderArticleDetail(data); // 받은 데이터를 템플릿에 적용하는 함수 호출
}

function renderArticleDetail(article) {
    // 받은 데이터를 템플릿에 적용하여 세부 정보를 표시하는 코드 작성
    document.getElementById("article-title").innerText = article.title;
    document.getElementById("article-content").innerText = article.content;
    document.getElementById("article-author").innerText = article.author;
    document.getElementById("article-created-at").innerText = article.created_at;
    // 필요에 따라 추가적인 정보들을 처리할 수 있습니다.
}

window.onload = fetchTravelDetail;
