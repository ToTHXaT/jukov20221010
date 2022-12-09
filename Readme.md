# Запуск контейнера:

Для запуска необходимо загрузить файл docker-compose и запустить его с помощью команды
```shell
    docker-compose up
```

### Настройка реплик

Для создания дополнительных реплик в файл docker-compose.yml нужно добавить следующее 
```
    deploy:
      mode: replicated
      replicas: 4
```
Где **mode** отвечает за режим работы (global либо replicated), что указывает docker'у либо создавать одну копию на узел, либо несколько.
А **replicas** отвечает за количество этих реплик отвечает за количество этих реплик.
### Создани swarm'а

Инициализируем swarm
```shell
    docker swarm init
```

### Запуск приложения

Запускаем приложение:
```
    docker stack deploy --compose-file docker-compose.yml jukov-task9-swarm
```

Проверяем работу 
```shell
    curl localhost:5010/
```

### Остановка работы

Остаавливаем приложение
```shell
    docker stack rm jukov-task9-swarm
```

Выходим из swarm'а
```shell
   docker swarm leave --force
```
