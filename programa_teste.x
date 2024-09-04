int function funcaoTeste1(tmp param1: int, tmp param2: float){
    tmp soma:int;
    cte name:string;
    name = "programa teste";
    print(name);
    while(soma < 100){
        if (soma <= 90 || param1 > 20){
            soma = soma + 10;
        }
        else{
            soma >> 2;
            break;
        }
    }
    soma = 22 + 33 + 22;
    return soma;
}; 