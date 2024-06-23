"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio


import jsonplaceholder_requests
import models


async def async_main():
    async with models.Session() as session:

        users_json = await jsonplaceholder_requests.fetch_json(
            jsonplaceholder_requests.USERS_DATA_URL
        )

        posts_json = await jsonplaceholder_requests.fetch_json(
            jsonplaceholder_requests.POSTS_DATA_URL
        )

        users_list = list()
        for json_obj in users_json:
            filtered_fields = dict(
                {
                    "name": json_obj.pop("name"),
                    "username": json_obj.pop("username"),
                    "email": json_obj.pop("email"),
                    "id": json_obj.pop("id"),
                }
            )

            users_list.append(models.User(**filtered_fields))

        posts_list = list()
        for json_obj in posts_json:
            filtered_fields = dict(
                {
                    "user_id": json_obj.pop("userId"),
                    "title": json_obj.pop("title"),
                    "body": json_obj.pop("body"),
                }
            )

            posts_list.append(models.Post(**filtered_fields))

        await models.create_users(session=session, users=users_list)
        await models.create_posts(session=session, posts=posts_list)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
