document.getElementById('follow-button').addEventListener('click', async function() {
    try {
        const username = document.getElementById('username').textContent;
        const accessToken = localStorage.getItem('access_token');

        const response = await axios.post(`/api/users/follow/${username}/`, null, {
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });

        const detail = response.data.detail;
        if (detail === 'Followed successfully.' || detail === 'Unfollowed successfully.') {
            // 팔로우 상태가 업데이트되었으므로 UI를 업데이트합니다.
            document.getElementById('follow-button').textContent = (detail === 'Followed successfully.') ? '언팔로우' : '팔로우';
        } else {
            console.error('Follow error:', response.statusText);
            alert('팔로우 요청이 실패했습니다.');
        }
    } catch (error) {
        console.error('Follow error:', error);
        alert('팔로우 요청이 실패했습니다.');
    }
});

