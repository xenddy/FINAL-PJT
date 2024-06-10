const BASE_URL = "http://127.0.0.1:8000/";

async function fetchTravelArticles() {
    const response = await fetch(`${BASE_URL}api/articles/Leisure/`);
    const html = await response.text(); // HTML 형식의 데이터를 받음
    return html;
}

// 클릭 이벤트 핸들러 함수를 수정하여 바로 새 글 작성 페이지로 이동하도록 설정
function handleNewPostClick() {
    window.location.href = `${BASE_URL}newlist/`; // 새 글 작성 페이지로 이동
}

// 버튼 이벤트 리스너를 등록
document.getElementById("new-post-btn").addEventListener("click", handleNewPostClick);

async function initialize() {
    const html = await fetchTravelArticles();
    document.getElementById("articles-container").innerHTML = html; // 받은 HTML을 컨테이너에 삽입
}
