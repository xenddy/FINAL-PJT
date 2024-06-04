document.getElementById('logout-button').addEventListener('click', async function() {
    try {
        // 로컬 스토리지에서 refresh token을 가져오기
        const refreshToken = localStorage.getItem('refresh_token');
        
        // 로그아웃 요청
        await axios.post('/api/users/logout/', {
            refresh: refreshToken
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // 로컬 스토리지에서 토큰 제거
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');

        // 로그인 페이지로 리디렉션
        window.location.href = '/users/login/';
    } catch (error) {
        console.error('Logout error:', error);
        alert('로그아웃 실패: ' + JSON.stringify(error.response.data));
    }
});