#!/usr/bin/guile-2.0 -s !#

(use-modules (ice-9 rdelim))


;;;; An awful blogware for my niche purposes. 
;;;; Will come back and fix up later into my journey with Guile Lisp.

(define alist '())


(define (template template-file html-file)
	(format #t "Processing ~A...~%" template-file)
	(let ((port (open-input-file template-file)))
		(define empty "")
		(define line (read-line port))
		(while (not (eof-object? line))
			(let ((l-index (string-index line #\~)))
				(cond ((not (eq? l-index #f))
					(set! line (string-replace line 
						(assoc-ref alist (substring line l-index 
									(+ (string-rindex line #\~) 1)))
						l-index (+ (string-rindex line #\~) 1)))
					(set! line (string-append/shared line "\n"))
					(set! empty (string-append/shared empty line)))
				(else (set! line (string-append/shared line "\n"))
					(set! empty (string-append/shared empty line)))))

			(set! line (read-line port)))
		(format #t "Finished processing ~A.~%" template-file)
		(format #t "Writing to ~A...~%" html-file)

		(let ((out-port (open-output-file html-file)))
			(format out-port "~A" empty)
		(close-port out-port))

	(close-port port))
(format #t "All done.~%"))




(define (mark-down in-file)
	(format #t "Processing ~A...~%" in-file)

	(let ((port (open-input-file in-file)))
		(define line (read-line port))
		(define value "")

		(let ((key (string-copy line))) ; Key to the key value pair.	
			;; So it doesn't set the first line twice.
			(set! line (read-line port))
	
			(while (not (eof-object? line))
				(cond ((eq? (string-ref line 0) #\tab)
					(set! value
						(string-append/shared 
							value line)))
				(else
					(set! alist (acons key value alist))
					(set! key line)	(set! value "")))	
				(set! line (read-line port)))
			(set! alist (acons key value alist)))	
		(close-port port))
	(format #t "Finished processing ~A.~%" in-file))
