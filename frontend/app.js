// Главное приложение Mini App
const app = document.getElementById('app');

// ======== API URL backend ========
const API_URL = 'https://YOUR_RAILWAY_BACKEND_URL'; // Заменить на реальный URL после развёртывания

// Навигация по страницам через hash
function loadPage() {
    const hash = window.location.hash || '#courses';
    fetchPage(hash);
}

// Загружаем HTML страницы в #app
function fetchPage(page) {
    let pageFile = page.substring(1) + '.html';
    fetch(`pages/${pageFile}`)
        .then(response => response.text())
        .then(html => {
            app.innerHTML = html;
            if (page === '#courses') loadCourses();
            if (page === '#services') loadServices();
            if (page === '#giveaways') loadGiveaways();
            if (page === '#about') loadAbout();
            if (page === '#account') loadAccount();
        })
        .catch(err => {
            app.innerHTML = '<h2>Страница не найдена</h2>';
            console.error(err);
        });
}

// ======== КУРСЫ ========
async function loadCourses() {
    try {
        const response = await fetch(`${API_URL}/courses/`);
        const courses = await response.json();

        const container = document.getElementById('courses-container');
        container.innerHTML = '';

        courses.forEach(course => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${course.title}</h3>
                <p>${course.short_description}</p>
                <p>Цена: ${course.price} ₽</p>
                ${course.is_promo ? `<p>Старая цена: ${course.old_price} ₽ - Акция!</p>` : ''}
                <button class="button" onclick="alert('Запись на курс: ${course.title}')">Записаться</button>
            `;
            container.appendChild(card);
        });

    } catch (error) {
        console.error('Ошибка загрузки курсов:', error);
    }
}

// ======== УСЛУГИ ========
async function loadServices() {
    try {
        const response = await fetch(`${API_URL}/services/`);
        const services = await response.json();

        const container = document.getElementById('services-container');
        container.innerHTML = '';

        services.forEach(service => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${service.title}</h3>
                <p>${service.short_description}</p>
                <p>Цена: ${service.price} ₽</p>
                <button class="button" onclick="alert('Обсудить услугу: ${service.title}')">Обсудить детали</button>
            `;
            container.appendChild(card);
        });

    } catch (error) {
        console.error('Ошибка загрузки услуг:', error);
    }
}

// ======== РОЗЫГРЫШИ ========
async function loadGiveaways() {
    try {
        const response = await fetch(`${API_URL}/giveaways/`);
        const giveaways = await response.json();

        const container = document.getElementById('giveaways-container');
        container.innerHTML = '';

        giveaways.forEach(giveaway => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${giveaway.title}</h3>
                <p>${giveaway.description}</p>
                <button class="button" onclick="alert('Участвовать в розыгрыше: ${giveaway.title}')">Участвовать</button>
            `;
            container.appendChild(card);
        });

    } catch (error) {
        console.error('Ошибка загрузки розыгрышей:', error);
    }
}

// ======== ОБО МНЕ ========
function loadAbout() {
    const container = document.getElementById('about-container');
    container.innerHTML = `
        <img src="assets/alexandra.jpg" alt="Александра" style="max-width:100%; border-radius:12px;">
        <p>Привет! Я Александра, визажист с многолетним опытом...</p>
        <button class="button" onclick="window.location.href='https://t.me/AlexandraTelegram'">Связаться со мной</button>
    `;
}

// ======== ЛИЧНЫЙ КАБИНЕТ ========
async function loadAccount() {
    try {
        const response = await fetch(`${API_URL}/course_access/`);
        const courses = await response.json();

        const container = document.getElementById('account-container');
        container.innerHTML = '';

        if (courses.length === 0) {
            container.innerHTML = `
                <p>У вас пока нет купленных курсов. Посмотрите коллекцию!</p>
                <a class="button" href="#courses">К курсам</a>
            `;
        } else {
            courses.forEach(course => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <h3>${course.title}</h3>
                    <button class="button" onclick="window.open('${course.youtube_playlist}', '_blank')">Открыть видеоуроки</button>
                    <button class="button" onclick="window.open('${course.google_drive}', '_blank')">Скачать материалы</button>
                    <button class="button" onclick="window.open('${course.telegram_channel}', '_blank')">Перейти в чат курса</button>
                `;
                container.appendChild(card);
            });
        }

    } catch (error) {
        console.error('Ошибка загрузки личного кабинета:', error);
    }
}

// Обработчик изменения hash
window.addEventListener('hashchange', loadPage);

// Первичная загрузка
window.addEventListener('load', loadPage);
