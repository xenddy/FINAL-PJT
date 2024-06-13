const axiosInstance = axios.create({
    baseURL: 'http://3.38.93.229/',
})

document.addEventListener('DOMContentLoaded', async function() {
    try {
        // URL에서 username 파라미터를 가져오기
        const path = window.location.pathname;
        const username = path.split('/').filter(Boolean).pop();
        
        // 로컬 스토리지에서 access token을 가져오기
        const accessToken = localStorage.getItem('access_token');
        
        // 사용자 정보 요청
        const response = await axios.get(`/api/users/${username}/`, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });

        const userData = response.data;
        
        // 사용자 정보 표시
        document.getElementById('username').textContent = userData.username;
        document.getElementById('first-name').textContent = userData.first_name;
        document.getElementById('date-joined').textContent = new Date(userData.date_joined).toLocaleDateString();
    
    } catch (error) {
        console.error('Error fetching user details:', error);
        alert('사용자 정보를 가져오는 데 실패했습니다.');
    }
});

