drop database if exists Casino;
create database Casino;
use Casino;

create table jugadores(
id_jugador int auto_increment primary key,
nombre varchar(30) not null,
apellido varchar(30) not null,
dni varchar(20),
fecha_nacimiento date,
saldo Decimal(10,2) default 0
);
create table membresias(
id_membreia int auto_increment primary key,
id_jugador int not null,
nivel varchar(50),
fecha_inicio date,
fecha_vencimiento date, 
foreign key (id_jugador) references jugadores(id_jugador)
);
create table transacciones(
id_transaccion int auto_increment primary key,
id_jugador int not null,
tipo varchar(30) not null,
monto decimal(10,2) not null,
fecha_hora datetime,
foreign key (id_jugador) references jugadores(id_jugador)
);
create table puestos(
id_puesto int auto_increment primary key,
puesto varchar(100) not null
); 
create table crupieres(
id_crupier int auto_increment primary key,
nombre varchar(50) not null,
apellido varchar(50),
id_puesto int,
turno varchar(50),
foreign key (id_puesto) references puestos(id_puesto)
);
create table juegos(
id_juego int auto_increment primary key,
id_crupier int,
nombre_juego varchar(100) not null,
tipo varchar(50),
min_apuesta decimal(10,2),
max_puesta decimal(10,2),
foreign key (id_crupier) references crupieres(id_crupier)
);
create table mesas(
id_mesa int auto_increment primary key,
id_juego int,
ubicacion varchar(100),
capacidad int,
foreign key (id_juego) references juegos(id_juego)
);
create table apuestas(
id_apuesta int auto_increment primary key,
id_jugador int not null,
id_juego int,
monto decimal(10,2) not null,
fecha_hora datetime,
resultado varchar(100),
foreign key (id_jugador) references jugadores(id_jugador),
foreign key (id_juego) references juegos(id_juego)
);
create table premios(
id_premio int auto_increment primary key,
id_apuesta int not null,
monto_ganado decimal(10,2) not null,
foreign key (id_apuesta) references apuestas(id_apuesta)
);

insert into jugadores (nombre, apellido, dni, fecha_nacimiento, saldo) values
('Juan', 'Pérez', '30555111', '1990-04-12', 1500),
('María', 'Gómez', '29888777', '1988-09-21', 3200),
('Carlos', 'Luna', '31544333', '1995-12-02', 800);

insert into membresias (id_jugador, nivel, fecha_inicio, fecha_vencimiento) values
(1, 'Oro', '2024-01-01', '2025-01-01'),
(2, 'Plata', '2024-03-10', '2025-03-10'),
(3, 'Bronce', '2024-04-05', '2025-04-05');

insert into puestos (puesto) values
('Ruleta'),
('Blackjack'),
('Poker');

insert into crupieres (nombre, apellido, id_puesto, turno) values
('Sofía', 'Martínez', 1, 'Mañana'),
('Lucía', 'Fernández', 2, 'Tarde'),
('Diego', 'Ramos', 3, 'Noche');

insert into juegos (id_crupier, nombre_juego, tipo, min_apuesta, max_apuesta) values
(1, 'Ruleta', 'Ruleta', 50, 5000),
(2, 'Blackjack', 'Blackjack', 100, 3000),
(3, 'Poker', 'Poker', 200, 20000);

insert into mesas (id_juego, ubicacion, capacidad) values
(1, 'Sala A', 6),
(2, 'Sala B', 5),
(3, 'Sala C', 8);

insert into apuestas (id_jugador, id_juego, monto, fecha_hora, resultado) values
(1, 1, 200, '2024-05-12 15:30:00', 'Ganó'),
(1, 2, 100, '2024-05-12 16:10:00', 'Perdió'),
(2, 3, 500, '2024-05-13 18:45:00', 'Ganó'),
(3, 1, 50, '2024-05-14 20:00:00', 'Perdió');

insert into premios (id_apuesta, monto_ganado) values
(1, 400),
(3, 1200);

-#Nombre del jugador y el nombre del juego en cada apuesta#-
select j.nombre, g.nombre_juego
from apuestas a
inner join jugadores j on j.id_jugador = a.id_jugador
inner join juegos g on g.id_juego = a.id_juego;

-#Jugador y su nivel de membresía#-
select j.nombre, j.apellido, m.nivel
from jugadores j
inner join membresias m on m.id_jugador = j.id_jugador;

-#Jugadores con apuestas superiores a 100#-
select j.nombre, j.apellido, a.monto
from apuestas a
inner join jugadores j on j.id_jugador = a.id_jugador
where a.monto > 100;

-#Listado de mesas con su juego y crupier#-
select m.id_mesa, g.nombre_juego, c.nombre as crupier
from mesas m
inner join juegos g on g.id_juego = m.id_juego
inner join crupieres c on c.id_crupier = g.id_crupier;

-#Jugadores que retiraron plata#-
select 
    j.id_jugador,
    j.nombre,
    j.apellido,
    t.id_transaccion,
    t.monto,
    t.fecha_hora
from transacciones t
inner join jugadores j on j.id_jugador = t.id_jugador
where t.tipo = 'retiro';

-#Crupieres y los puestos en los que trabajan#-
select 
    c.nombre,
    c.apellido,
    p.puesto
from crupieres c
inner join puestos p on p.id_puesto = c.id_puesto;

-#Jugador que mas plata gano en el juego#-
	select j.id_jugador, j.nombre, j.apellido, sum(p.monto_ganado) as total_ganado
from jugadores j
inner join apuestas a on a.id_jugador = j.id_jugador
inner join premios p on p.id_apuesta = a.id_apuesta
inner join juegos g on g.id_jue--go = a.id_juego
where g.nombre_juego = 'Ruleta'
group by j.id_jugador, j.nombre, j.apellido
order by total_ganado desc
limit 1;

-#Total de apuestas y promedio de plata por juego#-
select g.id_juego, g.nombre_juego,
       count(a.id_apuesta) as cantidad_apuestas,
      avg(a.monto) as promedio_monto
from juegos g
inner join apuestas a on a.id_juego = g.id_juego
group by g.id_juego, g.nombre_juego
order by promedio_monto desc;


