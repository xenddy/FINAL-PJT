const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
})

document.getElementById('signup-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const firstName = document.getElementById('first_name').value;

    const csrfToken = window.CSRF_TOKEN;

    try {
        const response = await axios.post('/api/users/', {
            username: username,
            password: password,
            first_name: firstName,

        });

        console.log('Signup successful:', response.data);
        window.location.href = '/login/';
    } catch (error) {
        console.error('Signup error:', error.response.data);
        alert('회원가입 실패: ' + JSON.stringify(error.response.data));
    }
});
