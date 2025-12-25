// Главный скрипт админки
const adminContent = document.getElementById('admin-content');
const API_URL = 'https://YOUR_RAILWAY_BACKEND_URL'; // заменяем на реальный URL после развёртывания

// Загрузка контента по hash
function loadAdminPage() {
    const hash = window.location.hash || '#dashboard';

    switch(hash) {
        case '#dashboard':
            loadDashboard();
            break;
        case '#users':
            loadUsers();
            break;
        case '#courses':
            loadCoursesAdmin();
            break;
        case '#services':
            loadServicesAdmin();
            break;
        case '#giveaways':
            loadGiveawaysAdmin();
            break;
        case '#posts':
            loadPostsAdmin();
            break;
        case '#requests':
            loadRequestsAdmin();
            break;
        case '#settings':
            loadSettingsAdmin();
            break;
        default:
            adminContent.innerHTML = '<h2>Раздел не найден</h2>';
    }
}

// ======== ЗАГРУЗКА РАЗДЕЛОВ ========
function loadDashboard() {
    adminContent.innerHTML = '<h2>📊 Дашборд</h2><p>Ключевая статистика будет здесь.</p>';
}

async function loadUsers() {
    try {
        const res = await fetch(`${API_URL}/users/`);
        const users = await res.json();
        let html = '<h2>👥 Пользователи</h2><table><tr><th>Имя</th><th>Telegram</th><th>Дата регистрации</th></tr>';
        users.forEach(u => {
            html += `<tr><td>${u.name}</td><td>${u.telegram}</td><td>${u.registered_at}</td></tr>`;
        });
        html += '</table>';
        adminContent.innerHTML = html;
    } catch (err) {
        console.error(err);
        adminContent.innerHTML = '<p>Ошибка загрузки пользователей</p>';
    }
}

async function loadCoursesAdmin() {
    try {
        const res = await fetch(`${API_URL}/courses/`);
        const courses = await res.json();
        let html = '<h2>✨ Курсы</h2>';
        courses.forEach(c => {
            html += `<div class="card"><h3>${c.title}</h3><p>${c.short_description}</p><p>Цена: ${c.price}</p></div>`;
        });
        adminContent.innerHTML = html;
    } catch (err) {
        console.error(err);
        adminContent.innerHTML = '<p>Ошибка загрузки курсов</p>';
    }
}

async function loadServicesAdmin() {
    try {
        const res = await fetch(`${API_URL}/services/`);
        const services = await res.json();
        let html = '<h2>📅 Услуги</h2>';
        services.forEach(s => {
            html += `<div class="card"><h3>${s.title}</h3><p>${s.short_description}</p><p>Цена: ${s.price}</p></div>`;
        });
        adminContent.innerHTML = html;
    } catch (err) {
        console.error(err);
        adminContent.innerHTML = '<p>Ошибка загрузки услуг</p>';
    }
}

async function loadGiveawaysAdmin() {
    try {
        const res = await fetch(`${API_URL}/giveaways/`);
        const giveaways = await res.json();
        let html = '<h2>🎁 Розыгрыши</h2>';
        giveaways.forEach(g => {
            html += `<div class="card"><h3>${g.title}</h3><p>${g.description}</p></div>`;
        });
        adminContent.innerHTML = html;
    } catch (err) {
        console.error(err);
        adminContent.innerHTML = '<p>Ошибка загрузки розыгрышей</p>';
    }
}

async function loadPostsAdmin() {
    try {
        const res = await fetch(`${API_URL}/posts/`);
        const posts = await res.json();
        let html = '<h2>📿 Посты</h2>';
        posts.forEach(p => {
            html += `<div class="card"><h3>${p.title}</h3><p>${p.content}</p></div>`;
        });
        adminContent.innerHTML = html;
    } catch (err) {
        console.error(err);
        adminContent.innerHTML = '<p>Ошибка загрузки постов</p>';
    }
}

async function loadRequestsAdmin() {
    try {
        const res = await fetch(`${API_URL}/requests/`);
        const requests = await res.json();
        let html = '<h2>📋 Заявки</h2>';
        requests.forEach(r => {
            html += `<div class="card"><p>${r.name} — ${r.type} — ${r.item}</p></div>`;
        });
        adminContent.innerHTML = html;
    } catch (err) {
        console.error(err);
        adminContent.innerHTML = '<p>Ошибка загрузки заявок</p>';
    }
}

function loadSettingsAdmin() {
    adminContent.innerHTML = '<h2>⚙️ Настройки</h2><p>Настройки админки и текста бота здесь.</p>';
}

// Обработчик изменения hash
window.addEventListener('hashchange', loadAdminPage);
window.addEventListener('load', loadAdminPage);
