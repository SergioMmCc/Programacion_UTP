#lang racket

#|Construya un programa en donde en una ventana 800*600
se dibuje un pixel en la posicion (0, 50), luego debe
dibujarse otro pixel en la posicion (1,50), (2,50), (3,50)
hasta llegar a la posicion (800,50). Use recursividad|#

(require (lib "graphics.ss" "graphics"))
(open-graphics)
(define Ventana (open-viewport "Cuadro" 800 600))

(define (pixel posx posy)
  (cond
    [(= posx 800) ((draw-pixel Ventana) (make-posn posx posy) "blue")]
    [else ((draw-pixel Ventana) (make-posn posx posy) "blue")
          (pixel (+ 1 posx) posy)]
    ))

#|(pixel (floor(* 800 (random))) (floor (* 600 (random))))|#


#|Dibujar 5 lineas de forma recursiva en distintas partes
de la ventana (Usar la funcion (random)). |#

(define (lineas posx posy cont)
    (cond
     [(= cont 5) (pixel posx posy)]
     [else (pixel posx posy) (lineas (+ (floor (* 800 (random)))(- posx 1000)) (+ (floor (* 600 (random))) (- posy 1000)) (+ 1 cont))
           ]))

(lineas 300 200 0)


#|(define (linea1 x y cont)
  (cond
    [(= cont 100) ((draw-pixel Ventana) (make-posn x (floor (* 600 (random)))) "blue")]
    [else ((draw-pixel Ventana) (make-posn x (floor (* 600 (random)))) "blue")
          (linea1 x (+ 1 y) (+ 1 cont))]))

(linea1 50 20 0)|#

#|(define (lineas2 x y cont cont2)
  (cond
    [(= cont 5) (linea1 x y cont)]
    [else (linea1 x y cont)
          (lineas2 x y cont (+ 1 cont2))]))

(lineas2 20 40 0 0)|#