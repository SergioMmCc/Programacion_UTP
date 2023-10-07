#lang racket

(require (lib "graphics.ss" "graphics"))
(open-graphics)
(define Ventana (open-viewport "Cuadro" 800 600))



(define (linea x1 y1 lim)
    (cond
    [(> x1 lim) void]
    [else ((draw-pixel Ventana) (make-posn x1 y1) "black") (linea (+ 1 x1) y1 lim)]
    )
)

(define (randlines n)
    (cond
    [(= n 0) void]
    [else (linea 0 (floor (* (random) 600)) 800) (randlines (- n 1))]
    )
)


(randlines 5)