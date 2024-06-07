const BASE_URL = "http://127.0.0.1:8000/";

async function fetchCampingArticles() {
    const response = await fetch(`${BASE_URL}api/articles/Camping/`);
    if (!response.ok) {
        throw new Error(`Failed to fetch articles: ${response.statusText}`);
    }
    const data = await response.json();
    return data;
}

// 클릭 이벤트 핸들러 함수를 수정하여 바로 새 글 작성 페이지로 이동하도록 설정
function handleNewPostClick() {
    window.location.href = `${BASE_URL}api/articles/newlist/`; // 새 글 작성 페이지로 이동
}

// 버튼 이벤트 리스너를 등록
document.getElementById("new-post-btn").addEventListener("click", handleNewPostClick);

async function initialize() {
    try {
        const articles = await fetchCampingArticles();
        const container = document.getElementById("articles-container");
        container.innerHTML = ""; // 초기화

        if (articles.length === 0) {
            container.innerHTML = "<tr><td colspan='1'>게시글이 없습니다.</td></tr>";
        } else {
            articles.forEach(article => {
                const row = document.createElement("tr");
                const cell = document.createElement("td");
                const link = document.createElement("a");
                link.href = `${BASE_URL}api/articles/Camping/${article.id}/`;
                link.textContent = article.title;
                cell.appendChild(link);
                row.appendChild(cell);
                container.appendChild(row);
            });
        }
    } catch (error) {
        console.error('Error initializing articles:', error);
    }
}

initialize();
