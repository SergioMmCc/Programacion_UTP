#lang racket
(define (impuestos edad ingresos)
  (cond
    [(and (> edad 16)(>= ingresos 1000)) "Debe tributar"]
    [else "No debe tributar"]
    )
  )

(define (precio edad2)
  (cond
    [(< edad2 4) "La entrada es gratuita"]
    [(and (>= edad2 4)(<= edad2 18)) "La entrada vale $5000"]
    [(> edad2 18) "La entrada vale $10000"]
    ))

(define (monto area presupuesto)
  (cond
    [(equal? area "ginecologia")(* presupuesto 0.35)]
    [(equal? area "traumatologia")(* presupuesto 0.25)]
    [(equal? area "pedriatria")(* presupuesto 0.3)]
    ))

(define (triangulo a b c)
  (cond
    [(and (= a b)(= b c)) "Equilatero"]
    [(or (= a b)(= b c)(= a c)) "Isosceles"]
    [(and (not (= a b))
          (not (= a c))
          (not (= b c))) "Escaleno"]
    ))