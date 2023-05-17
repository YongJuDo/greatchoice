// document.addEventListener('DOMContentLoaded', () => {
//     const likeForm = document.querySelector('.likeForm');
//     const likeCount = document.querySelector('.likeCount');
//     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// likeForm.forEach((likeForm) => {
//     likeForm.addEventListener('submit', (event) => {
//         event.preventDefault();

//         const reviewPk = likeButton.dataset.reviewPk;

//         axios({
//         method: 'post',
//         url: `/reviews/review_like/${reviewPk}/`,
//         headers: { 'X-CSRFToken': csrftoken },
//         })
//         .then((response) => {
//             const likeCountText = response.data.like_users_count;

//             likeCount.textContent = likeCountText;