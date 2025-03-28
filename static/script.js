document.getElementById('feedback-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const feedbackMessage = document.getElementById('feedback-message');

    try {
        const response = await fetch(form.action, {
            method: form.method,
            body: formData
        });

        const result = await response.json();
        if (response.ok) {
            feedbackMessage.style.color = 'green';
            feedbackMessage.textContent = 'Спасибо за ваш отзыв!';
            form.reset();
        } else {
            feedbackMessage.style.color = 'red';
            feedbackMessage.textContent = result.message || 'Ошибка при отправке отзыва.';
        }
    } catch (error) {
        feedbackMessage.style.color = 'red';
        feedbackMessage.textContent = 'Ошибка: ' + error.message;
    }
});