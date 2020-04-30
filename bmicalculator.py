def regnBmi():
    print("Vennligst skriv inn din vekt(kg): ")
    v = float(input())
    print("Vennligst skriv inn din høyde(m): ")
    h = float(input())

    bmi = (v/(h*h))
    
    if bmi <= 18.4:
        print("Din BMI er:", str((round(bmi,2))))
        print("Kategori:Undervekt")
        print("Sykdomsrisiko: Lav for diabetes, økt for andre helseproblemer")
    elif bmi >= 18.5 and bmi <= 24.9:
        print("Din BMI er:", str((round(bmi,2))))
        print("Kategori:Normalvekt")
        print("Sykdomsrisiko: Lav")
    elif bmi >= 25.0 and bmi <= 29.9:
        print("Din BMI er:", str((round(bmi,2))))
        print("Kategori:Overvekt")
        print("Sykdomsrisiko: Økt for diabetes")
    elif bmi >= 30.0 and bmi <= 34.9:
        print("Din BMI er:", str((round(bmi,2))))
        print("Kategori:Fedme, grad 1")
        print("Sykdomsrisiko: Økt for diabetes, økt dødelighet")
    elif bmi >=35.0 and bmi <= 39.9:
        print("Din BMI er:", str((round(bmi,2))))
        print("Kategori:Fedme, grad 2")
        print("Sykdomsrisiko: Høy risiko for flere helseproblemer, Økt dødelighet")
    elif bmi >= 40.0:
        print("Din BMI er:", str((round(bmi,2))))
        print("Kategori:Fedme, grad 3")
        print("Sykdsomsrisiko: Ytterligere økt helserisiko")

regnBmi()
