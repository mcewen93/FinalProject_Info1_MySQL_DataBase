-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-12-2018 a las 05:43:24
-- Versión del servidor: 10.1.32-MariaDB
-- Versión de PHP: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `informatica1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `numactivo` int(20) NOT NULL,
  `serial` varchar(20) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `nomequipo` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `marca` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `codubicacion` int(5) NOT NULL,
  `codresp` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`numactivo`, `serial`, `nomequipo`, `marca`, `codubicacion`, `codresp`) VALUES
(1000, 'RX0001', 'Maquina de Rayos X', 'Phillips', 3, 1),
(1001, 'DESF0001', 'Desfribrilador', 'Phillips', 1, 5),
(1002, 'HEMO0001', 'Maquina de Hemodialisis', 'Bayer', 5, 2),
(1003, 'INC0001', 'Incubadora', 'Drager', 2, 4),
(1004, 'MONVIT0001', 'Monitor de Signos Vitales', 'Mindray', 4, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `responsables`
--

CREATE TABLE `responsables` (
  `codigo` int(50) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `id` int(20) NOT NULL,
  `cargo` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `responsables`
--

INSERT INTO `responsables` (`codigo`, `nombre`, `apellido`, `id`, `cargo`) VALUES
(1, 'David', 'McEwen Arango', 1122334401, 'Supervisor Traumatologia'),
(2, 'Daniel Alexander', 'Basto Moreno', 1122334402, 'Supervisor Cuidado Renal'),
(3, 'Angelower', 'Santana', 1122334403, 'Bioingeniero supervisor'),
(4, 'Kimberly', 'Sanchez', 1122334404, 'Coordinadora Sala de Neonatos'),
(5, 'Manuel Elkin', 'Patarroyo', 1122334405, 'Coordinador Salas de Cirugia y UCI');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicacion`
--

CREATE TABLE `ubicacion` (
  `codigoubic` int(11) NOT NULL,
  `nomubic` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `piso` int(11) NOT NULL,
  `telefono` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `ubicacion`
--

INSERT INTO `ubicacion` (`codigoubic`, `nomubic`, `piso`, `telefono`) VALUES
(1, 'Urgencias', 1, 3455555),
(2, 'Asistencia Neonatal', 5, 3455556),
(3, 'Traumatologia', 2, 3455557),
(4, 'Cirugia', 3, 3455558),
(5, 'Cuidado Renal', 4, 3455559);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`numactivo`);

--
-- Indices de la tabla `responsables`
--
ALTER TABLE `responsables`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD PRIMARY KEY (`codigoubic`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `numactivo` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81009092;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
