from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()









@app.get('/user/admin')
async def admin():
    return {"Вы вошли как администратор"}
# gt (greater than больше),
# ge (greater than or equal больше или равно),
# lt (less than меньше), и le (less than or equal меньше или равно)
@app.get('/user/{user_id}')
async def user_id(
        user_id: Annotated[int, Path(ge=0,
                                     le=100,
                                     description='Enter User ID',
                                     example='1')]
):
    return {f"Вы вошли как пользователь {user_id}"}

@app.get('/user/{username}/{age}')
async def user(
        username: Annotated[str, Path(min_length=3,
                                     max_length=20,
                                     description='Enter username',
                                     example='UrbanUser')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter age',
                                 example='24')]
):
    return {f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


@app.get('/')
async def welcome(): #-> dict:
    return {'Главная страница'}

