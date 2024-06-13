const BASE_URL = 'http://3.38.93.229/';

document.addEventListener('DOMContentLoaded', function() {
    const travelButton = document.getElementById('travel-button');
    const campingButton = document.getElementById('camping-button');
    const leisureButton = document.getElementById('leisure-button');
    const cookingButton = document.getElementById('cooking-button');

    // 카테고리 버튼 클릭 이벤트 리스너 등록
    travelButton.addEventListener('click', function() {
        window.location.href = `${BASE_URL}api/articles/Travel/`;
    });

    campingButton.addEventListener('click', function() {
        window.location.href = `${BASE_URL}api/articles/Camping/`;
    });

    leisureButton.addEventListener('click', function() {
        window.location.href = `${BASE_URL}api/articles/Leisure/`;
    });

    cookingButton.addEventListener('click', function() {
        window.location.href = `${BASE_URL}api/articles/Cooking/`;
    });

    fetchLatestPosts();
});

async function fetchLatestPosts() {
    try {
        const categories = ['Travel', 'Camping', 'Leisure', 'Cooking'];
        const latestPostsContainer = document.getElementById('latest-posts-container');
        latestPostsContainer.innerHTML = '';

        for (const category of categories) {
            console.log(`Fetching latest posts for category: ${category}`);
            const response = await fetch(`${BASE_URL}api/articles/latest/${category}/`);
            if (!response.ok) {
                throw new Error(`Failed to fetch ${category} posts`);
            }
            const posts = await response.json();
            console.log(`Posts for category ${category}:`, posts);
            const categoryTitle = document.createElement('h3');
            categoryTitle.textContent = category;
            latestPostsContainer.appendChild(categoryTitle);

            posts.forEach(post => {
                const postDiv = document.createElement('div');
                const postTitle = document.createElement('a');
                postTitle.href = `${BASE_URL}api/articles/${category}/${post.id}/`;
                postTitle.textContent = post.title;
                postDiv.appendChild(postTitle);
                latestPostsContainer.appendChild(postDiv);
            });
        }
    } catch (error) {
        console.error('Error fetching latest posts:', error);
    }
}
