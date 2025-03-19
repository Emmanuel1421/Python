try{
    var a=
    ["34","32","5","31","24","44","67"];
    console.log(a);
    console.log(b);
} catch (e) {
    console.log("Mensagem de erro: "+e.message);
}

let num="A";
try{
    if(isNaN(num)) throw "não é um número!"
    else if (num>40) throw "maior que 40,"
    else if (num<=30) throw "Menor que 30."
    else console.log("blz!")
}catch(e){
    console.log(e);
}

var vitor =['val1','val2','val3'];

vitor[20]="texto";

console.log(vitor);

var pessoa = ['Josélio','Alberisto','Jonas'];
pessoa.splice(2,0,"Alberto","Joca");
console.log(pessoa);


var novaPessoa = pessoa.slice(1,3);
console.log(novaPessoa);
