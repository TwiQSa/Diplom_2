
URL_USER_CREATION = 'https://stellarburgers.nomoreparties.site/api/auth/register' #Создание пользователя
URL_USER_LOGIN = 'https://stellarburgers.nomoreparties.site/api/auth/login' #Логин пользователя
URL_USER_DATA_UPDATE = 'https://stellarburgers.nomoreparties.site/api/auth/user' #Изменение данных пользователя
URL_ORDER_CREATION = 'https://stellarburgers.nomoreparties.site/api/orders' #Создание заказа (Если ручка POST)
URL_GET_USER_ORDERS = 'https://stellarburgers.nomoreparties.site/api/orders' #Получение заказов конкретного пользователя (Если ручка GET)


ORDER_WITHOUT_INGREDIENT = "Ingredient ids must be provided" #Если не передать ни один ингредиент
USER_ALREADY_EXISTS = "User already exists" #Если пользователь существует
INCOMPLETE_DATA_FOR_REGISTRATION = "Email, password and name are required fields" #Если нет одного из полей
INCORRECT_DATA_FOR_LOGIN = "email or password are incorrect" #Если логин или пароль неверные или нет одного из полей
WITHOUT_AUTH = "You should be authorised" #Если выполнить запрос без авторизации

correct_ingredients_for_order_creation = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa75"]} #Существующие элементы для создания бургера
incorrect_ingredients_for_order_creation = {"ingredients": ["spicybun123","sweetgalacticalsauce9021"]} #Несуществующие элементы для создания бургера