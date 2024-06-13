
const axiosInstance = axios.create({
    baseURL: 'http://`3.38.93.229`/',
});

document.getElementById('login-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    console.log(username, password);
    
    try {
        const res = await axiosInstance.post('/api/users/login/', { username, password });

        // 토큰 저장
        const accessToken = res.data.access;
        const refreshToken = res.data.refresh;

        // Axios 기본 헤더에 Authorization 설정
        axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;

        // 로컬 스토리지에 토큰 저장
        localStorage.setItem('access_token', accessToken);
        localStorage.setItem('refresh_token', refreshToken);

        console.log(axiosInstance.defaults.headers.common['Authorization']);
        console.log(res.data);

        // 로그인 성공 시 사용자 상세 페이지로 리디렉션
        window.location.href = `/users/${username}/`;
    } catch (error) {
        console.error('Login error:', error);
        alert('로그인에 실패했습니다.');
    }
});
