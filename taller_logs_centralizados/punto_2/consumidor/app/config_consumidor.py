class ConsumerConfig:
    SECRET_KEY ='mypass'

consumer_conf = {
    'bootstrap.servers': 'localhost:29092',
    'group.id': 'mi_grupo',
    'auto.offset.reset': 'earliest'
}
