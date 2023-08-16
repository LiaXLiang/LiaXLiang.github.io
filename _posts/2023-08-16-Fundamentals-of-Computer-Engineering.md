---
markmap:
  colorFreezeLevel: 2
---

# Zahlendarstellungen

## Grundlagen
- $\sum_b$ = {0,1,..., b-1} wobei b Basis(基数)genannt wird 
  - z.B. b-adische(元) Zahlen mit endlicher Wortlänge n: <br> $\sum_b^n$: 00456 $\in$ $\sum_{10}^5$ := alle Dezimalzahlen der Länge 5
  
    - Darstellbarkeit
      - Sei b $\in$ N mit b>1, dann ist jede natürliche Zahl *z* mit 0 $\le$ z $\le$ $b^n$-1 (und n $\in$ N) eindeutig als Wort der Länge <br>n über $\sum_b^n$ darstellbar durch **z = $\sum_{i=0}^{n-1}$ z<sub>i</sub> * b<sup>i</sup> mit z<sub>i</sub> $\in$ $\sum_b$ = {0,1,...,b-1} für i = 0,1,...,n-1**
  
   - Umrechnung
     - i.)  整数10进制-2进制: 逐步除以2，**由下到上**取余(最先被除后所剩余数位分最低-最先被淘汰)
     - ii.) 整数10进制-11进制：逐步除以11，也是**由下到上**取余
       - z.B. ==(2595)<sub>10</sub> = (1A4A)<sub>11==
     - iii.) 小数10进制-2进制：逐步乘2, **由上到下**取整(最先乘2所得的整数位分最高）
       - z.B. ==(0,6875)<sub>10</sub> = 0,(1011)<sub>2== <br>0.6875 * 2 = 1.375 <br> 0.375 * 2 = 0.75 <br> 0.75 * 2 = 1.5 <br> 0.5 * 2 = 1.0 
   
   - Arithmetische Operationen 
     - Addition
       - 进位/Übertrag Prinzip: Modolo-Operation
         - z.B. Resultat von <em>x+y</em> ist definiert für *n* Bits als **(x+y) mod 2<sup>n</sup>** <br> (1+1)mod 2 = 0 and (1+0) mod 2 = 1. (同理比如十进制下9+2得结果为1 => (9+2) mod 10 = 1)
     - Multiplikation
       - z.B. 二进制下==(1101*1001)<sub>2</sub>==<br>1001:= Multiplikand; 1001:= Multiplikator (乘数), wie Schulmethode. Resultat ==(1110101)<sub>2</sub>== 
   


## Darstellung ganzer Zahlen im Rechner 
- Wir arbeiten hauptsächlich auf der Menge B = {0,1}.  B<sup>n</sup> beschreibt dann die Menge der **n-stelligen Binärzahlen.** <br> Sei x = (x<sub>n-1</sub> ... x<sub>0</sub>) $\in$ B<sup>n</sup> eine **n-stellige Binärzahl**.
  
     - Vorzeichenlose Zahl 
       - 即无论MSB(Most Significant Bit)是0还是1，直接进行计算
         - z.B. Bei einer 8-Bit-Architektur wird ==(10010011)<sub>2</sub>== interpretiert als vorzeichenlose Zahl ==(147)<sub>10</sub>==

     - Einer-Komplement von x
        - • K<sub>1</sub>(x):= $\overline{x}$
            - (0???)<sub>2</sub> := wie im **vorzeichenlosen** Fall.  
            - (1???)<sub>2</sub> := Bilde Einerkomplement K<sub>1</sub>
               - z.B. Bei einer 8-Bit-Architektur wird  ==(10010011)<sub>2</sub>== interpretiert im Einerkomplement als ==(-108)<sub>10</sub>== (不要忘记写负号!!!)
          
        - Darstellungsbereiche: ==-(2<sup>n-1</sup>-1) $\le$ x $\le$ (2<sup>n-1</sup>-1)== <br> 解释：若不考虑负数情况，(n-Bits)<sub>2</sub>本应表示（0 ~ 2<sup>n</sup>-1)<sub>10</sub>，即可以表示#2<sup>n</sup>个十进制数字；但要分成两半分别表示正负数 => 2<sup>n-1</sup>个含零正数与2<sup>n-1</sup>个含零负数，包含了两次0。<br>如 n = 4时采用K<sub>1</sub>系统，(0000 ~ 0111)<sub>2</sub>表示(0 ~ +7)<sub>10</sub>；(1000 ~ 1111)表示(**-7 ~ -0**)<sub>10</sub>，导致效率低下。
     
     - Zweier-Komplement von x
       - • K<sub>2</sub>(x):= K<sub>1</sub>(x)+1 <br>i.) (1???)<sub>2</sub> 二进制到十进制 -> 减1再取反 <br>ii.)负数十进制到二进制 -> 取反再加1
          - z.B. Bei einer 8-Bit-Architektur wird ==(10010011)<sub>2</sub>== interpretiert im Zweierkomplement als ==(-109)<sub>10</sub>== 
       
       - Darstellungsbereiche: ==-(2<sup>n-1</sup>) $\le$ x $\le$ (2<sup>n-1</sup>-1)== (Wegen der **doppelten Darstellung der 0 im Einerkomplement** lässt sich im Zweierkomplement eine Zahl mehr darstellen.) <br>解释：结合Einerkomplement中 n = 4, K<sub>2</sub>系统去掉了用(1111)<sub>2</sub>来表示(-0)<sub>10</sub>的情况，可以在进位跳转时 [即(1000)<sub>2</sub>] 多表示一个数字[表示(-8)<sub>10</sub>]


- BCD-Code/Binary Coded Decimal/二进制码十进制数
   - Definition: <br>Ziffern werden einzeln mit 4 Bits als **vorzeichenlose** Binärzahl dargestellt. <br>（以4位二进制表示1个十进制数字：数值逻辑电路以二进位方式工作；输入输出以十进位方法表示） 
      - z.B. (4739)<sub>10</sub> = 0100 0111 0011 1001<sub>(2)</sub>
  
   - Problem：<br> i.) 1位十进制数字最大为(9)<sub>10</sub>，而4位二进制最大可表示(15)<sub>10</sub>；也就是说从(1010)<sub>2</sub> <=> (10)<sub>10</sub>起到(1111)<sub>2</sub> <=> (16)<sub>10</sub>起有6个Bitmuster ungenutzt <br> ii.)两个BCD数相加时如果和小于(1010)<sub>2</sub> <=> (10)<sub>10</sub>的话则无须修正，否则数字无意义
      - Solution: i.) 用两个二进制数作为Vorzeichen： (1010)<sub>2</sub> <=> (10)<sub>10</sub>表示正数；(1011)<sub>2</sub> <=> (11)<sub>10</sub>表示负数 <br> ii.) Korrektur: Bei jedem Übertrag und bei jeder ungültigen BCD-Darstellung 6 aufaddieren. 
         - 解释：如四位二进制计算下的(0011 + 1000)<sub>2</sub>，(3 + 8)<sub>10</sub>，结果本应为（1011)<sub>2</sub> <br>But this number is meaningless. It has to move forward a round (which means, move past 6 numbers) to find its right position in those nine meaningful binary numbers. So the correct answer is (1011 + 0110 = 0001)<sub>2</sub>，然后再向再上一部分的计算进1.如此循环。
        - e.g. (4739 + 1287)<sub>10</sub>  BCD-Calculation: (0100 0111 0011 1001 + 0001 0010 1000 0111)<sub>2</sub>, instead of the superficial result (0101 1001 1100 0000)<sub>2</sub>, the correct answer is (0110 0000 0010 0110)<sub>2</sub> which represents (6026)<sub>10</sub>.
   
   - Pros & Cons
      - pros: <br> i.) easy to encode & decode decimals into BCD and vice versa;<br>ii.) simple to implement a hardware algorithm for the BCD converter; <br>iii.) useful in digital systems whenever decimal information is given either as inputs or displayed as outputs
      - cons: <br>i.) BCD code for a given decimal number requires more bits than the straight binary code and hence there is difficulty to represent the BCD form in high speed digital computers in arithmetic operations, especially when the size and capacity of their internal registers are restricted or limited; <br> ii.) The arithmetic operations using BCD code requires a complex design of **Arithmetic and Logic Unit(ALU)** than the straight binary number system <br>iii.) The speed of the arithmetic operations that can be realized using BCD code is naturally slow due to the complex hardware circuitry involved. 

- Gray Code / 格雷码
  - Definition: <br> an ordering of the binary numeral system such that two successive values differ in only one bit (binary digit). <br> 任意两个相邻数的代码只有一位二进制数不同的编码  
    - z.B. 1,2,3,4 := 001,011,010,110
  - Constructing an n-bit Gray code 
    - I. Zahl im Binärcode darstellen 
      - (3)<sub>10</sub> $\qquad$  x<sub>1</sub> = (011)<sub>2</sub> 
    - II. Links-Schift um 1 Bit, x<sub>2</sub> = x<sub>1</sub> <<1
      - x<sub>2</sub> = (110)<sub>2</sub>  
    - III. XOR-Knüpfung  x<sub>3</sub> = x<sub>1</sub> $\bigoplus$ x<sub>2</sub>
      - x<sub>3</sub> = (101)<sub>2</sub> 
    - IV. Rechts-Schift um 1 Bit, x<sub>4</sub> = x<sub>3</sub> >>1  
      - x<sub>4</sub> = (010)<sub>2</sub>



## Darstellung der Kommazahlen im Rechner

- Festkomma-Darstellung(定点数 / fix point)
   - Definition: Fest vorgegebene Anzahl an Vor- und Nachkommastellen; getrennt voneinander binär dargestellt <br>约定计算机中小数点的位置，且此位置固定不变；小数点的前后数字分别用二进制表示然后组合起来 
     - z.B. Verwende 4 Bits für Vor- und 3 Bits für Nachkommateil (约定小数点位置) <br> 3.5 + 2.5 = (0011).(100) + (0010).(100) = (0110).(000) = (6.0)<sub>10</sub>
     - Pros & Cons
        - pros: suitable for representing integers in registers(寄存器)； easy to represent because it uses only one field, i.e. magnitude field
        - cons: range of representable number is restricted;  difficult to represent complex fractional number; no standard representation for fixed point representation


 - Gleitkomma-Darstellung (浮点数 / float point)<br>**IEEE754 (The IEEE Standard for Floating-Point-Arithmetic)** 

   - Definition: <br> IEEE754规定了四种表示浮点数值的方式：单精确度（32位）、双精确度（64位）、延伸单精确度（43比特以上，很少使用）与延伸双精确度（79比特以上，通常以80位实现)
      - 实际值: Jede Zahl *z* wird in der Form **z = $\pm$m * b<sup>$\pm$e</sup>** dargestellt mit *m Mantisse(尾数)，e Exponent(指数)，b Basis(基数) für die Exponenten*
      - Rechnen mit Gleitkommazahlen
        - Definition:<br> Mit x ,y $\in$ R ist das Ergebnis einer IEEE754 Operation $\circ$ $\in$ {+,-,*,/} definiert als *round(x $\circ$ y)*. IEEE754 definiert nicht, wie exakt gerundet werden muss, sondern liefert Alternativen. D.h. die gleichen 32-Bit FP-Operationen können unterschiedliche Ergebnisse liefern, obwohl korrekt (den Standard befolgend).
        - z.B. Rundung: round to nearest(tie to even)/四舍五入到最接近的偶数；e.g. 1.50 $\mapsto$ 2 <br>round to nearest (tie away from zero) e.g. 2.50 $\mapsto$ 3, -1.5 $\mapsto$ -2；<br> round toward zero e.g. -1.5 $\mapsto$ -1；<br>round down; round up(取整后的数总是$\geqslant$ 原数) 
      
    - Speicherung einer Gleitkommazahl in <em>drei</em> Felden(域)
        - 最高有效位(MSB)：被指定为符号位( sign bit / Vorzeichen )
           - 0 bei positive Zahlen und 1 bei negative Zahlen 
        
        - 指数域：[即次高有效的k个比特]存储指数部分
           - • 指数偏移值(Exponent Bias)：==指数域的编码值 ê = 指数的实际值 e + 偏移值 Bias==
             - 为什么指数要用移码而不是带符号位置的原码或补码？<br>——简化浮点数的运算和大小比较。我们对浮点数进行大小比较时，其实就是比较两个科学记数法表示的数字，所以首先要比较他们的数量级(由指数e决定)。<br>I.) 假设采用带符号位的原码表示，首先要检查符号位，若不相同，则正数>负数；若同正则绝对值大的数比较大；若同负则绝对值较小的数比较大，对此需要实现两套比较逻辑以应对两种不同的情况。实现时导致CPU电路复杂。<br> II.) IEEE754规定将指数e加上Bias再存储，移码ê的取值范围$\ge$0，无需考虑同异号，由于都是正数所以采用同一套比较电路即可，简化了CPU的设计
           
           - • 规约形式浮点数 / Normalisierte Darstellung
              - Definition: <br> i.) 指数域的编码值不全为0$\land$不全为1 [ê $\neq$ (0...0) and ê $\neq$ (1...1)]，即(0 < ê $\le$ **2<sup>k</sup>-2**)；<br> ii.) 小数点处于尾数最高有效位的左侧，同时在小数点左侧有一位隐含的二进制有效整数1
                - IEE754规定规约形式浮点数 ==Bias = 2<sup>k-1</sup>-1==，其中k为存储指数的比特的长度   
                   - 解释: i.) 编码值ê值域(vorzeichenlos) [0 , 2<sup>k</sup>-1]；为处理指数为负数的情况使用编码值ê区间[0, 2<sup>k-1</sup>-1]来存储负数(含0)指数；使用编码值ê区间[2<sup>k-1</sup> , 2<sup>k</sup>-1]来存储正数指数(不含0)           <br> ii.) 对应的指数实际值e值域分别为[-(2<sup>k-1</sup>-1) , 0] , [1 , 2<sup>k-1</sup>]  
                - 为什么默认小数点左侧有隐含的1？
                  - 浮点数在内存中的表示其实就是二进制的科学计数法。<br>十进制下科学计数法为了达到最高效地表示数字的目的，不允许有效数字的整数部分为0，整数部分为0时通过改变数量级指数来调整，使得整数部分变成1-9之间的整数：如0.365 * 10<sup>5</sup>要写成3.65 * 10<sup>4</sup>     <br>二进制下的科学计数法同理，如(111010)<sub>2</sub>的二进制科学计数法是1.11010 * 2<sup>5</sup>而不是0.111010 * 2<sup>6</sup>；由于二进制只有0和1两种数字，所以二进制数的科学计数法中，有效数字的整数部分永远为1。有了这个结论后其实就没有必要花内存去存有效数字开头的这个1了，只存有效数字的小数部分(.11010)即可
           - • 非规约形式浮点数 / Denormalisierte Darstellung 
              - Definition: <br> i.)指数域的编码值全为0，尾数部分非0；<br>ii.) ==Denomaliserte的指数Bias比Normalisierte的指数Bias**小1**== <br> iii.) Mantisse m = $\widehat{m}$ ohne führende 1. [z = 0,$\widehat{m}$] 
                - 一般是某个数字相当接近0时才会使用非规约形式来表示，由此来解决填补绝对值意义下最小规格数与0的距离.
                
        - 尾数域：[即最后剩下的n个**最低有效位(LSB)**的比特]存储小数部分  
    - e.g. 32位单精度 & 64位双精度浮点数
      - 32位单精度 / IEEE754 32-Bit Single
         - 规约形式
            - 符号位：比特长度【1】，比特编号【31】
            - 指数位：比特长度==【8】==， 比特编号==【30 ～ 23】==, Bias = 2<sup>8-1</sup>-1 = ==127==
            - 尾数位：比特长度==【23】==，比特编号==【22 ～ 0】== * m wird intepretiert als m = 1 + (0,$\widehat{m}$) = 1,$\widehat{m}$, also 1$\le$m$<$2
         - Beispie
            - Rechnen Sie die im IEEE-754-Format angegebene Zahl ins Dezimalsystem um. 11000000100100101000000000000000  (注意最后基数b应该是2而不是10!!!)<br> Answer: **-4.578125**  
         - 特征值 
              - Kleinste normalisierte Zahl (Betrag): $\widehat{m}$ = (0...0), $\widehat{e}$ = (0...1) $\Rightarrow$ ==1.0 * 2<sup>-126</sup>==
              - Größte denormalisierte Zahl (Betrag): $\widehat{m}$ = (1...1), $\widehat{e}$ = (0...0) $\Rightarrow$ ==(0.11111111111111111111111)<sub>2</sub>  * 2<sup>-126</sup>==   
      
      - 64位双精度 / Double-precision floating point  
        - 规约形式
            - 符号位：比特长度【1】，比特编号【63】
            - 指数位：比特长度==【11】==， 比特编号==【62 ～ 52】==, Bias = 2<sup>11-1</sup>-1 = ==1023==
            - 尾数位：比特长度==【52】==，比特编号==【51 ～ 0】== * m wird intepretiert als m = 1 + (0,$\widehat{m}$) = 1,$\widehat{m}$, also 1$\le$m$<$2
    
    - 特征值
      - Sonderfall: Über-und Unterlauf (+$\infty$ oder - $\infty$)
        - Definition: <br> Das Resultat einer Gleitkomma-Operation ist zu groß, um es darzustellen (bzw. zu klein, dann Unterlauf)
        - Im IEEE754 wird es durch $\widehat{m}$ = (0...0) und einen Exponenten $\widehat{e}$ = (1...1) mit $\widehat{s}$ $\in$ {0,1} dargestellt.
      - NaN: Not a Number
        - Definition:<br> Das Resultat einer Gleitkomma-Operation ist keine gültige Gleitkommazahl. 
          - In mathematics, zero divided by zero is undefined and is therefore represented by NaN in computing systems. The square root of a negative number is not a real number, and is therefore also represented by NaN in compliant computing systems. NaNs may also be used to represent missing values in computations. 
         - NaN werden durch $\widehat{m}$ $\neq$ (0...0)und einen Exponente $\widehat{e}$ = (1...1) dargetellt.
    
    - Pros & Cons
      - pros: any type and any size of numbers can be represented easily; there are several standardized representation for it
      - cons: It is a complex representation as it uses two fields: mantissa and exponent;  Length of registres for storing floating numbers is large



# Booolesche Algebra/逻辑代数(A formalism for describing logical operations)<br>Definition:<br> i.) The values of the variables: the truth values *true(1)* and *false(0)*<br> ii.) Main operations: und$\land$, oder$\lor$, nicht$\lnot$  

- Schaltfunktionen <br>Definition: Seien n, m $\in$ N, n,m $\geqslant$ 1. Dann heißt eine Funktion *F* : B<sup>n</sup> $\to$ B<sup>m</sup> Schaltfunktion. <sub>(Input für den Rechner ist ein *n-Bit-Tupel*, Output ist ein *m-Bit-Tupel*)</sub> <br>z.B.  Multiplikation von zwei 16-stelligen Dualzahlen.(n = 32, m = 32) <br>Primzahltest einer 16-stelligen Dualzahl (n = 16, m = 1)<sub>1 falls Primzahl, 0 sonst</sub>

  - Boolesche Funktionen
    - Definition: Eine Schaltfunktion *f* : B<sup>n</sup> $\to$ B<sup>==1==</sup> heißt (n-stellige) Boolesche Funktion mit n $\in$ N, n $\geqslant$ 1 
    - Zusammenhang zu Schaltfunktionen:
      - Sei *F* : B<sup>n</sup> $\to$ B<sup>m</sup> mit *F* (x<sub>n-1</sub> ,..., x<sub>1</sub>, x<sub>0</sub>) = (y<sub>m-1</sub> ,..., y<sub>1</sub>, y<sub>0</sub>). Setzt man für jedes *i* $\in$ {m-1, ..., 0} *f<sub>i</sub>* : B<sup>n</sup> $\to$ B definiert durch *f<sub>i</sub>* (<sub>n-1</sub> ,..., x<sub>1</sub>, x<sub>0</sub>) = y<sub>i</sub>  <sub>(// boolesche Funktion berechnet das y<sub>i</sub> aus den n-stellige Eingabeswert. Die Schlatfunktion stellt sich dar als Tuplen von booleschen Funktionen)</sub>

    - Beispiele
      - 1-stellige Boolesche Funktion 
        - *F* : {0,1}$\to${0,1} $\qquad$ $\qquad$   f<sub>0</sub>(x) = 0; f<sub>1</sub>(x) = 1; f<sub>2</sub>(x) = x; f<sub>3</sub>(x) = $\bar x$
      
      - 2-stellige Boolesche Funktion
        - *F* : { (0,0),(0,1)(1,0)(1,1) }$\to${0,1} $\qquad$ insgesamt 16 Funktionen
      
      - =="3-valued logic/三值逻辑/ternäre Logiken== 
        - <br>sometimes abbreviated 3VL 
          - Any of several many-valued logic systems in which there are three truth values indicating true, false, indeterminant third value. 
          - Don't care term: a don't-care term for a function is an **input-sequence** (a series of bits) for which the function output does not matter.
      
      -  |  |  |  |  |  | funktional vollständig | 
         |:---:|:---:| :---:| :---:| :---:| :---:|
         | $\downarrow$    | $\overline{x+y}$  |  NOR  | nicht oder | f(0,0) = 1 | Ja, as well {$\lor$, $\lnot$}|
         | $\uparrow$      | $\overline{x•y}$  |  NAND | nicht and  | f(1,1) = 0 | Ja, as well {$\land$, $\lnot$}| 
         | x + $\bar x$    |  ≡1   |  | x • $\bar x$ | ≡0 |    
         | $\rightarrow$   |   $\bar x$ + y    | $\le$ | Implikation | f(1,0) = 0| {$\rightarrow$,1}, Nicht |
         | $\leftarrow$    |   x + $\bar y$    | $\geq$|             | f(0,1) = 0| {$\leftarrow$,$\lnot$ } Ja
         |                 | x $\bigoplus$ y   |  XOR  | $\neq$      | f(0,0) = f(1,1) = 0|
         - ==Funktionale Vollständigkeit==: 
           - Definition: Ein System B = {f<sub>1</sub> , ... , f<sub>n</sub>} heißt funktional vollständig, wenn sich jede Boolesche Funktion durch Einsetzungen bzw. Kompositionen von Funktionen aus *B* darstellen lässt. 
    
    - Darstellung Boolescher Funktionen 
      - DNF & KNF
        - Disjunkte Normalform  
          - Definition
            - A boolean function is expressed as ==a sum of minterms==, where each minterm corresponds to a row (of the function's truth table) whose output value is 1. (Minterm itself is a product term)<br> / DNF is a disjunction($\lor$ 或) of one or more conjunctions($\land$与) of one or more literals (an OR of ANDS). 
          - Kanonische DNF
            - Eine kanonische disjunktive Normalform (KDNF) ist eine DNF, die paarweise voneinander unterschiedliche Minterme enthält, in denen jede Variable genau ein Mal vorkommt. Sie wird auch vollständige disjunkte Normalform genannt. Jede Boolesche Funktion besitzt genau eine KDNF.
        
        - Konjunktive Normalform
          - Definition:
            - A boolean function is expressed as ==a product of maxterms==, where each maxterm corresponds to a row (of the function's truth table) whose output value is 0. (Maxterm itself is a sum term)
      
      - DAG-Darstellung / Directed-Acyclic-Graph / 有向无环图
          - Gatter /(logic) gate 
            - Definition: Eine Anordnung<sub>(arrangement)</sub> zur Realisierung einer booleschen Funktion, die binäre Eingangssignale durch Implementierung logischer Operatoren zu *einem* binären Ausgangssignal umgewandelt und auf das Ausgangssignal abgebildet. 
          
          - Anwendung: Schaltungsabhängige Fehlerdiagnose 
            - Annahmen: ① Es tritt im gegebenen Schaltnetz höchstens ein Fehler auf <br> ② Der Defekt, welcher den Fehler verursacht, ist ein gerissener Verbindungsdraht.
            - Verfahren: 
              - i.) Funktionen für alle Transitionen finden.
                - First we need to observe "DAG mit Drahtnummern". All wires should be checked (one wire at a time).
              - ii.) Fehlerklassen identifizieren
                - We start from wire1 and assume that wire is broken. Here "broken" means that no matter what the input is, always comes out 0. 
              - iii.) Wertetabellen für Fehlerklassen auftstellen(Ausfallmatrix) 
                - Then we can record these results by new indexed boolean functions, we list all of these new boolean functions using *Ausfalltafel/-matrix*. 
              - iv.) Fehlermatrix ausfüllen (durch XOR mit *f*)
                - We divide this Reduzierte Ausfallmatrix in three major columns, column1 := different possible inputs, i.e. Eingabe-Tupels; $\quad$ column2 := the original to-be-checked function; $\quad$ column3 := reduced new boolean functions (indexed by broken wires). In column3 we should record 0 if the outcome of this particular input is identical with that of the original boolean function (it is actually a $\bigoplus$ operator), 1 if different. i.e., it's where 1 stays that we should pay attention to. 
              - v.) Testsequenz erstellen 
          - *** Flimmerschaltung entspricht nicht irgendeiner Booleschen Funktion
      
      -  Binary Decision Diagrams / 二元决策图
         - Definition
           - BDD is a data structure used to represent a Boolean function. <sub>//Eine Zeile in der Wahrheitstabelle / Eine Belegung der Argumentvariablen entspricht einem Pfad in Baum.</sub> <br>标记有变量名字的圆形节点为内部节点，底部方形节点为终端节点(Blätter)。一个内部节点，若所标记变量的值为1则沿着实线弧前进；否则沿着虚线弧前进。给定一组变量值，计算函数*f*的值，只需从Wurzel沿着路径(Pfad)找到终端节点，终端节点的标记即为函数的值。
         - Reduction Rules
           - Rule#1 
             - Merge all terminal nodes 1 into one node, and merge all terminal nodes 0 into one node <sub>//die Blätter zusammenlegen</sub>
           - Rule#2: Verjüngung 4-3 Regel
             - <sub>// {(x,y) , (x,z)} we only keep 1 *x*-node instead of 2 *x*-nodes </sub>
           - Rule#3: Elimination 2-1 Regel
             - Remove redundant nodes. The node is redundant if its low and high successors are the same. <sub>// *f* = xy +  $\bar x$y = (x + $\bar x$)y = y Alles was heroben ankommt, geht direkt zu y-Knoten. </sub>
      
    - Vereinfachung Boolescher Funktionen 
      - Terminology 
        - Resolutionsregel / 归结规则
          - ab + a$\bar b$ = a(b + $\bar b$) = a1 =a
        - Minimal Polynom / 极小多项式
          - Definition
            - Sei *M* ein Polynom für *f* : B<sup>n</sup> $\rightarrow$ B<sup>1</sup>  <br> M heißt Minimalpolynom für *f*, wenn es kein Polynom geringerer Länge für *f* gibt. 
              - Polynom := DF := Sum of products (SoP) 
              - die Länge eines Polynoms := die Anzahl der Literale, die es enthält   
              - Literale := Variablensymbol + gegebenfalls Negation
                - z.B. x<sub>1</sub>, $\overline {x3}$ sind Literal, aber x<sub>1</sub> + $\overline {x3}$ ist kein Literal, es besteht aus 2 Literal. <sub>//Literl berücksicht nicht auf die Operatoren, es werden nur die Variablenzeichen gezählt </sub> 
        - Implikant / 涵项
          - Definition
            - Implicant is a "product term"/minterm in Sum of Products(SoP) or "sum term"/maxterm in Products of Sums (PoS) of a Boolean function.   <br> Sei *f*: B<sup>n</sup> $\rightarrow$ B<sup>1</sup> eine Boolesche Funktion. Ein Term *P* $\neq$ 0 heißt Implikant von *f*, kurz P $\leq$ *f*, falls P(x) $\leq$ f(x) für alle x $\in$ B<sup>n</sup> gilt, d.h. P(x) = 1 $\Rightarrow$ f(x)=1 $\forall$x $\in$ B<sup>n</sup>    <br>在布尔逻辑的积项和式中，若P是乘积项，且对于使P得到值1的所有组合，*f*也等于1，则P是布尔函数*f*的涵项
              - e.g. *f* = AB + ABC + BC, implicants are AB, ABC and BC 

          - Primimplikant / 质涵项
            - A prime implicant of a function is an implicant that cannot be covered by a more reduced (i.e., with fewer literals) implicant. // The removal of any literal from P results in a non-implicant for *f*.    <br> Ein Implikant *P* von *f* heißt Primimplikant von *f*, falls keine echte Verkürzung von P noch Implikant von *f* ist.    <br> *f*的质涵项 := 最少化文字数量的涵项，即若从P去除任何Literal都导致P成为*f*的非涵项
              - (卡诺图中)A group of squares or rectangels made up of a bunch of adjacent minterms which is allowed by the definition of K-Map. i.e., all possible groups formed in K-Map. 
              - 若100和101是某逻辑函数的两个涵项，那么10x就是函数的一个质涵项，其中1和0两个数字不可再去掉 
          - Kernimplikant  / 基本质涵项
            - Essential prime implicants are prime implicants that cover an output of the function that no combination of other prime implicants is able to cover.  <br>Ein Kernimplikant *P* heißt Kernimplicant von *f*, falls P in jedem Minimalpolynom von *f* vorkommt. / Those prime implicants that always appear in the final solution. 
            - (卡诺图中) Subcubes that cover at least one minterm that can't be covered by any other prime implicant.
      - Karnaugh-Diagramme / Karnaugh map
        - Definition
          - 卡诺图是真值表的变形，它可以将有n个变量的逻辑函数的2<sup>n</sup>个最小项组织在给定的长方形表格中。
            - 复杂度：若需要处理的逻辑函数自变量较多（$\geq$5时）卡诺图的行列数将迅速增加
        - Construction
          - 行和列的indices (shown across the top and down the left side of the Karnaugh map)是以格雷码而不是二进制数字顺序排列的。Gray code ensures that only one variable changes between each pair of adjacent cells. Each cell of the completed Karnaugh map contains a biary digit representing the function's output for that combination of inputs.
        - Grouping / Blöckbildung
          - Adjacent 1s in the Karnaugh map represent opportunities to simplify the expression. The minterms for the final expression are found by encircling groups of 1s in the map.
            - i.) Minterm groups must be rectangular and must have an area that is a power of two (i.e., 1,2,4,8...)
            - ii.) Minterm rectangles should be as large as possible without containing any 0s.   
            - iii.) The grid is toroidally connected, which means that rectangular groups can wrap across the edges. Cells on the extreme right are actually 'adjacent' to those on the far left, in the sense that the corresponding input values only differ by one bit; similarly, so are those at the very top and those at the bottom.   
      - Quine-McCluskey-Verfahren / 奎因-麦克拉斯基算法
        - 复杂度：尽管在处理多于四个变量时比卡诺图更加实用，但奎因-麦克拉斯基算法的运行时间随输入大小而呈指数增长。
        - Verfahren
          
          - I. Das Quine-McCluskey-Verfahren geht nun von einer algebraischen Darstellung der Formel in kanonischer DNF aus. Eine solche KDNF besteht aus einer Disjunktion von mintermen. Eine andere Darstellung muss also zuerst in diese Form gebracht werden. 
          
          - II. Minterme gemäß Anzahl der Negationen
            - i.) All minterms are sorted by ascending class, listed in a table. The class of a conjunction is the number of negated variables occurring in it. 
            - ii.) 标题栏 Gruppe - Implikant - Index(dezimal) 
              - <sub>Index(dezimal) := 记录这一行minterme在十进制下的下标.   <br> z.B. Index栏中有11  $\Leftrightarrow$ Implikant栏中有1011，即x<sub>3</sub>$\bar x$<sub>2</sub> x<sub>1</sub>x<sub>0</sub>  $\Leftrightarrow$ Gruppe 1 </sub></sub>
          
          - III. Ermitteln der Primimplikanten
            - i.) Man vergleicht nun alle Minterme benachbarter Klassen daraufhin, ob sie sich paarweise um eine einzige Negation unterscheiden.   <br>Ist dies der Fall, so verschmilzt man die beiden Terme zu einem neuen term und trägt ihn in eine zweite Tabelle ein. Die beiden verwendeten Terme werden gekennzeichnet. 
              - 同时在Index栏中记录被合并的minterme下标 <br>e.g. 原属Gruppe1的x<sub>3</sub>x<sub>2</sub>x<sub>1</sub>$\bar x$<sub>0</sub>(Index14)和原属Gruppe2的x<sub>3</sub>x<sub>2</sub>$\bar x$<sub>1</sub>$\bar x$<sub>0</sub>(Index12)被合并到Gruppe1，此时Implikant栏中记录为x<sub>3</sub>x<sub>2</sub>$\bar x$<sub>0</sub>，同时在Index栏中记录12,14 $\qquad$
            - ii.) The procedure is applied recursively until no further "Verschmelzungen" are possible.  <sub>//man weißt noch nicht, ob die Kernimplikanten sind</sub>

          - IV. Erstellen der Implikationsmatrix
            - i.) Als Spaltenköpfe der Tabelle werden die (dezimal) Indizes der minterme verwendet. Als Zeilenköpfe trägt man die Primimplikante ein. Die einzelnen Zellen der Tabelle sind also Kreuzungspunkte bestimmter Minterme mit bestimmten Primimplikanten.
              - e.g. 接上例，原属Gruppe2的x<sub>3</sub>x<sub>2</sub>$\bar x$<sub>1</sub>$\bar x$<sub>0</sub>(Index12)也可以和属于Gruppe3的$\bar x$<sub>3</sub>x<sub>2</sub>$\bar x$<sub>1</sub>$\bar x$<sub>0</sub>(Index 4)合并到Gruppe2，此时Implikant栏中记录为x<sub>2</sub>$\bar x$<sub>1</sub>$\bar x$<sub>0</sub>，同时在Index栏中记录4，12 $\qquad$
              - 表格中Einträge 1 := 表头此列的minterm可由表头此行的Primimplikant表示；0反之
            - ii.) die Spalten paarweise vergleichen
              - <sub>看哪一列只有一个1，则这一个1所在行对应的Implikant braucht man unbedingt</sub>
            - iii.) die Zeilen paarweise vergleichen
              - <sub>看还需要剩余哪些Implikanten就可以abdecken alle übrigen Indizes</sub>
            - 最终Minimalpolynom := 每行每列只保留一个1；  Kernimplikant := originally in the Implikationsmatrix对应行与对应列只有一个1
      - //Bei Karnaugh-Diagramme & Quine-McCluskey-Verfahren kann man sicher sein, dass die Minimalpolynome rauskommen, bei OBDD ist das nicht garantiert, denn Variablenordnung bei OBDD ist relevant. 

# Elektronische Grundlagen
- Physikalische Grundlagen
  - ==Elektrische Ladung (Q)== / electric charge /电荷 
    - Definition
      - Electric charge is the physical property of matter that causes charged matter to experience a force when placed in an electromagnetic field.   <br> Electric charge can be positive or negative (commonly carried by protons and electrons respectively). Like charges repel each other and unlike charges attract each other. An object with an absence of net charge is referred to as neutral.
    - Einheit: 库仑 / C für "Coulomb" 
    - Das Phänomie geladener Materie lässt sich mit dem Atommodell(原子模型) erläutern
      - Terminology
        - Neutron / 中子
        - ==Ladungsträger== / charge carrier /载流子：可以自由移动的带有电荷的物质微粒 <br> Elektronen und Protonen sind sogenannte Ladungsträger. Sie können weder erzeugt noch vernichtet werden.
          - Proton / 质子: positiv geladen $\qquad$ Symbol: p<sup>+</sup> $\qquad$ Ladung eines Protons: e
          - Elektron / 电子: negativ geladen $\qquad$ Symbol: e<sup>-</sup>   $\qquad$ Ladung eines Elektrons: -e
        - Elementarladung / 基本电荷，也称元电荷
          - Definition: die kleinste frei existierende elektrische Ladungsmenge. <br> Ussually denoted by *e* is the electric charge carried by a single proton or, equivalently, the magnitude of the negative electric charge carried by a single electron, which has charge *−e*. This elementary charge is a fundamental physical constant.
          - *e* = 1,602•10<sup>-19</sup>C 
          - Ladung von Materie entsteht durch Verschiebung von Elementarladungen. 
          - Die elektrische Ladung Q eines Körpers ist quantisiert. Sie ist immer ein Vielfaches der Elementarladunge *e* : Q = n•e, n$\in$ $\mathbb N$
            - Wie groß ist n für 1C? —— ${1\over e}$  
    - Kraftwirkung durch Ladung
      - Körper mit gleicher Ladung stoßen sich ab. Ungleich geladene Körper ziehen sich an. 
      - Couloum-Gesetz
        - 库仑定律表明，在真空中两个静止点电荷之间的相互作用力，与两电荷间距离的平方成反比，且与两电荷电量的乘积成正比，作用力方向在它们的连线上，同号电荷相斥，异号电荷相吸 / Ungleichmäßig verteilte Ladungsträger suchen Ausgleich.
  
  - ==Elektrische Spannung== / Voltage / 电压  
    - Definition
      - 电压是两点之间的电位差（electric potential difference），也就是静电学中将一库仑试探电荷从一点移动到另外一点所需要的能量。<br> Energie, die als Ergebnis einer Ladungsträgerverschiebung bezogen auf die Ladungseinheit zur Verfügung steht. 
    - Symbol: Voltage difference is denoted symbolically by ΔV, simplified *V*, especially in English-speaking countries, or by *U* internationally, for instance in the context of Ohm's or Kirchhoff's circuit laws.
    - Einheit: 伏(特) / V für "volt" 
    - U = ${W \over Q}$
      - U steht für elektrische Spannung
        - [U] = J/C = V
          - 1V= 1W/A，即电场力将1库仑（C）正电荷由a点移至b点所做的功为1焦耳（J）时，a、b两点间的电压为1V。
      - W steht als potenzielle Energie (zum Ladungsträgerausgleich) zwischen zwei Punkten zur Verfügung 
        - [W] = J für "Joule" 
        - potenzielle Energie / potential energy / 势能： 势能是储存于一个系统内的能量，也可以释放或者转化为其他形式的能量。势能是状态量，又称作位能。势能不是属于单独物体所具有的，而是相互作用的物体所共有。
    - Spannung wirkt zwischen zwei Punkten eines Schaltkreises. In der Regel gibt man die Spannung eines Punktes *P* in einem Schaltkreis immer in Bezug auf einen **festen Nullpunkt** an. <br>Man spricht dann auch vom Potenzial(势)des Punktes *P*. Dieser Nullpunkt heißt in Schaltkreisen Masse(接地).
      - 比如分析电路的时候说某个节点的电压，就是在说这个节点和地（参考地）之间的电势差。这就像物体运动选择参考系一样，才有可比性。同理，电路中也需要定义一个参考点，便于我们分析。  
  
  - ==(Elektrische) Strom (I)== / (electric) current / 电流 
    - Definition
      - 电流 (electric current / Strom)
        - 电荷在电场或(半)导体内的平均定向移动。电流的方向，定义为正电荷移动的方向 <br>Elektrische Strom ist die gerichtete Bewegung von Ladungsträgern (d.h. in metallischen Leitern: Elektron)
      - 电流强度（current intensity / Stromstärke）
        - 电流的大小称为电流强度，指单位时间内通过导线某一截面的电荷净转移量，每秒通过1库仑的电荷量称为1安培。“电流强度”也常直接简称为“电流”或称为“电流量” <br> Die Stromstärke *I* ist die Menge der bewegten Ladung pro Zeiteinheit.
        - I = ${ΔQ \over Δt}$ 
    - Einheit: 安培 / A für "Ampere"
      - 1A = ${1C \over 1s}$
  - ==Elektrischer Widerstand (R)== / electrical resistance / 电阻
    - Definition
      - 电阻是一个物体对于电流通过的阻碍能力 <br> Der elektrischer Widerstand entsteht durch den Widerstand, der sich der Ausgleichsbewegung freier Ladungsträger entgegenstellt. 
    - Einheit: 欧姆 / c für "Ohm"
      - 1Ω = ${1V \over 1A}$ 
        - Wenn bei 1V Spannung ein Strom mit 1A Stromstärke fließt, dann hat der Leiter einen Widerstand von 1Ω.
    - Ohmsches Gesetz U = R•I
      - Der durch einen Widerstand R fließende Strom I wächst mit dem Wert der an dem Widerstand abfallenden Spannung U: I~U <sub>// I ist propotional zu U</sub>     


- Kirchhoffsche Regeln / 基尔霍夫定律
  - 基尔霍夫电流定律 / (Strom-)Knotenregel
    - Definition
      - 所有进入某节点的电流的总和等于所有离开这节点的电流的总和 <br> Die Summe aller einem Punkt *p* in einem Schaltkreis zufließenden Ströme ist gleich der Summe der von *p* abfließenden Ströme.
    - Die Maschenregel drück die Erhaltung von Ladungs aus.   
  
  - 基尔霍夫电压定律 / (Spannungs-)Maschenregel
    - Definition
      - 沿着闭合回路所有器件两端的电势差(电压)的代数和等于零。 <br> Die Summe aller in einer Masche *m* eines Schaltkreises abfallenden Spannungen ist gleich Null.
        - Masche := Mesh,	a group of branches within a network joined so as to form a complete loop such that there is no other loop inside it. 
    - Die Maschenregel drück die Erhaltung von Energie(能量守恒) aus.
  
  - Anwendung von Ohmschem Gesetz und Kirchhoff-Regeln 
    - Serienschaltung / 串联电路
      - 几个电路元件沿着单一路径互相连接，每个连接点最多只连接两个元件，此种连接方式称为串联。以串联方式连接的电路称为串联电路。连接点称为节点。<br>从串联电路的电源给出的电流等于通过每个元件的电流，给出的电压等于每个元件两端的电压的代数和。串联电路也被称为“分压电路”。 
    - Parallelschaltung / 并联电路
      - 几个电路元件的两端分别连接于两个节点，此种连接方式称为并联。以并联方式连接的电路称为并联电路。连接点称为节点。<br> 从并联电路的电源给出的电流等于通过每个元件的电流的代数和，给出的电压等于每个元件两端的电压。并联电路也被称为“分流电路”。   

# Kondensator und Spule
- ==Kondensator== / capacitor / 电容器
  - 基本概念 
    - Definition
      - Das Bauteil, das Energie in einem ==elektrischen Feld== speichern kann (durch Ladungsungleichverteilung) <br> 将电能储存在电场中的被动电子器件
    - Plattenkondensator
      - Intro
        - 电容器包括两个电极(本身是导体，电极的金属片通常用的是铝片或是铝箔)，两个电极之间由称为==介电质==的绝缘体隔开。
        - 电荷会储存在电极表面，靠近介电质的部份。
        - 二个电极储存的电荷大小相等，符号相反，因此电容器中始终保持为电中性。
      - Ladung beim Plattenkondensator
        - ==Q = $\frac {ε₀·εᵣ·A}{d}$·U==  
          - ε₀ ≈ 8.854·10⁻¹² $\frac {As}{Vm}$ := elektrische Feldkonstante
          - εᵣ := dimensionslose Größe
          - A := Fläche des Kreises
          - d := Abstand    
    - ==Elektrische Kapacität(C)== / capacitance / 电容
      - Definition
        - 电容 := 给定电压，电容器储存电荷的能力 <br> Kapazität *C* ist geometrie- und materialabhängige Bauteileigenschaft eines Kondensators 
      - Einheit: 法拉 / F für "Farad"
        - C= $\frac {Q}{U}$ 
          - 两片导板分别载有负电荷与正电荷，所载有的电荷量分别为-$Q$,+$Q$；两片导板之间的电位差/电压为$U$, 则此电容器的电容为C= $\frac {Q}{U}$ 
          - Bei einer Ladung von 1C bzw. -1C auf den beiden Platten fällt an einem Kondensator mit 1F genau 1V Spannung ab.  <br>1法拉(Farad)等于1库仑(Coulomb)每伏特(Voltage)。在正常状况下1法拉的电容多加1伏特的电位差可以多储存1库仑的电荷。 

    - 电容器的电势能<br>the energy stored in a capacitor
      - ==W<sub>charging</sub> = $\frac {1}{2}$C·V² = U<sub>stored</sub>==
        - 电容器所储存的能量等于充电所做的功。平行板电容器，搬移微小电荷元素$dq$从带负电薄板到带正电薄板，每对抗1伏特的电位差，需要做功$dW$ = $\frac {q}{c}$dq
        - 将此方程式积分可得到储存于电容器的能量。从尚未充电的电容器(q=0)开始，搬移电荷从带负电薄板到带正电薄板，直到这两片薄板分别拥有电荷量 $-Q$, $+Q$ 所需要做的功为
   - Kondensatorschaltungen 
     - 多个电容器串并联(Parallelschaltung)
       - Q<sub>ges</sub> = $\sum_{i=1}^{n}$ Qᵢ
       - C<sub>ges</sub> = $\sum_{i=1}^{n}$ Cᵢ
         - 电容器并联后容量明显变大，但耐压以最小电容的耐压为准 
     - 多个电容器串联(Reihenschaltung)
       - Q<sub>ges</sub> = Q₁ = ... = Qₙ
       - $\frac {1}{Cges}$ = $\sum_{i=1}^{n}$ 1/Cᵢ
   - Schaltverhalten eines Kondensators
     - ==**i(t) = i₀·e<sup>-$\frac {t}{τ}$</sup>**== 
       - Die Zeitkonstante τ gibt an, wie schnell ein Kondensator geladen oder entladen wird.    

- ==Spule== / Electromagnetic coil
  - 基本概念
    - Definition
      - Das Bauteil, das Energie in Form eines ==magnetischen Feldes== speichern kann.  
    - Zylindersplule / 螺线管 
    - Terminology
      - ==Magnetischer Fluss(Φ<sub>B</sub>)== / Magnetic flux / 磁通量
        - 是通过某给定曲面的磁场(亦称为磁通量密度）的大小的度量。
        - Einheit: 韦伯 / Wb für "Weber" <br>1Wb = 1Vs
          - ==Φ = $\frac {L·I}{N}$==  
            - L := Induktivität
            - I := Strom
            - N := Anzahl der Windungen
      
      - ==Magnetische Flussdichte(B)== / Magnetic Flux Density / 磁感应强度
        - 磁感应强度 := 磁通量密度或磁通密度,表示贯穿一个标准面积的磁通量的物理量

      - 楞次定律 / Lenz's Law
        - Die *induzierte Spannung* erzeugt einen ***Induktionsstrom***, der so gerichtet ist, dass sein *magnetisches Fled* der Flussänderung, die ihn verursacht hat, entgegen wirkt. <br>感应电流具有这样的方向，即感应电流的磁场总要阻碍引起感应电流的磁通量的变化。 
      - die im Magnetfeld gespeicherte Energie nach vollständigem Aufladen des Feldes mit einem Strom
        - ==E = $\frac 1{2}$L·I²==  
      
      - ==Induktivität(L)== / Inductance / 电感
        - Definition
          - 电感是闭合回路的一种属性，即当通过闭合回路的电流改变时，会出现电动势来抵抗电流的改变。这种电感称为自感（self-inductance），是闭合回路自己本身的属性。<br>假设一个闭合回路的电流改变，由于感应作用而产生电动势于另外一个闭合回路，这种电感称为互感(mutual inductance)。
        - Einheit: 亨利 / H für "Henry"
          - ==L = N² $\frac{μ₀·μᵣ·A}{l}$==
            - μ₀ ≈ 4π·10⁻⁷$\frac {H}{m}$ := magnetische Feldkonstante
            - μᵣ := materialabhängige Konstante
          - H = $\frac {Wb}{A}$  
            - Bei einer Stromänderung von 1 Ampere in einer Sekunde fällt an einer Spule 1H genau 1V Selbstinduktionsspannung ab. 

# Halbleiter
- Intro
  - In metallischen Leitern (金属导体) bilden die Atome ein Kristallgitter(晶格), in dem sich Eleketron frei bewegen können; Bei Nichtleitern sind die Elektronen dagegen fest an die Atome gebunden. 

- Modell
  - das Bohrsche Atommodell / 玻尔模型
    - Intro
      - ① Die Elektronen können sich innerhalb der Atomhülle(原子壳层) in verschiedenen Schalen (Energieniveaus) bewegen. 
        - ==Energieniveaus / 能级 / energy level==
          - 描述微观粒子体系（原子、电子、分子等）可能存在的相对稳定状态下，所对应一系列不连续的、分立的且确定的“内在”能量值或状态。<br>能级理论则是一种解释原子核外电子运动轨道的理论。它认为电子只能在特定的、分立的轨道上运动，各个轨道上的电子具有分立的能量，这些能量值即为能级。由于距原子核越远的电子越不受束缚，因此其能级越高，该电子具有越多的电子能量。  
      - ② Befindet sich ein Elektron in einem Atom (z.B. Wasserstoffatom氢原子) auf der 1. Schale, dann befindet sich das Elektron im ==Grundzustand(基态)==
        - 基态：在量子力学里，一个系统可能处于一系列量子态中的一个。这一系列的量子态依能量（能阶）多少排列，其中能量最少的量子态称为基态。具有更高能量的状态称为激发态。系统一般倾向于占据能量最少的状态，所以基态是研究一个量子系统的重要方面。 
      - ③ Nur diskrete Energieniveaus sind möglich. Die Energieniveaus werden in Elektronenvolt (eV) angegeben.
        - 在玻尔模型里，被约束于原子壳层的带负价电子，绕着带正价原子核进行圆周运动。从一个轨道跃迁至另一个轨道会伴随着==离散能量==以电磁波的形式被发射或吸收。  
        - ==Elektronenvolt / 电子伏特==
          - 能量单位；代表一带电荷量为1.602•10<sup>-19</sup> (1e)库仑的电子在真空中通过1伏特电位差所产生的动能(W=Q·U)
      - ④ Die Energiedifferenz $\triangle$W zwischen zwei Energieniveaus ist stets diskret 
    - e.g. 硅
      - Atommodell von Silicium / 硅原子模型: $\quad$ Das Silicium-Atom hat vier Valenzelektron
      - Kristallaufbau von Silicium / 晶体硅: $\quad$ Die Valenzelektronen bilden mit den Valenzelektronen der vier benachbarten Silicium-Atome gemeinsame Elektronenpaare. 
  - Energiebändermodell / 能带理论 
     - Intro
       - ① 价电子 / ==Valence electron== 
         - 所有固体物质都是由原子组成的，而原子则由原子核和电子组成。原子核外的电子在以原子核为中心的轨道上运动，距离原子核越远的轨道其能级（电位能的级别）越高，电子也就越容易脱离原子的束缚，变成可以运动的自由电子。<br> 最外层的电子最活跃，决定了与其他原子结合的方式（化学键），决定了该元素的化学性质，也就决定了该原子的价值，因此被称作为“价电子”。
       - ② 能带
         - 当原子处于孤立状态时，其电子能级可以用一根线来表示；当若干原子相互靠近时，能级组成一束线；当大量原子共存于内部结构规律的晶体中时，密集的能级就变成了带状，即能带。电子先占据低能量的能带，逐步占据高能级的能带。<br> 原子的电子状态决定了物质的导电特性，而能带就是在半导体物理中用来表征电子状态的一个概念。能带论是目前研究固体中的电子状态，说明固体性质最重要的理论基础。
       - ③ 根据电子填充的情况，能带分为
         - ==Leitungsband / 传导带 / conduction band==
           - 指半导体或绝缘体材料中，一个电子所具有能量的范围。这个能量的范围高于价电带。
             - 材料的导电性是由“传导带”中含有的电子数量决定。当电子从“价带”获得能量而跳跃至“传导带”时，在外电场的作用下，未填满的传导带能带中的电子产生净电流，材料表现出导电性。 
         - ==Bandlücke / 带隙 / band gap== 
           - 泛指半导体或绝缘体的价带顶端至传导带底端的能量差距 
             - 能带结构可以解释固体中导体(没有能隙)、半导体(能隙 < 3eV)、绝缘体 (能隙 > 3eV)三大类区别的由来。<br> 绝缘体的带隙很宽，电子很难跃迁到导带形成电流，因此绝缘体不导电。<br> 金属导体只是价带的下部能级被电子填满，上部可能未满，或者跟导带有一定的重叠区域，电子可以自由运动，即使没有重叠，其带隙也是非常窄的，因此很容易导电。<br> 半导体的带隙宽度介于绝缘体和导体之间，其价带是填满的，导带是空的，如果受热或受到光线、电子射线的照射获得能量，电子容易跃迁到导带中，因而导电性能容易发生大的变化。
         - ==Valenzband / 价电带 / valence band==
           - 指半导体或绝缘体材料中，在0K时能被电子占满的最高能带。若给价电带上的电子一个高于能隙的能量，该电子便会跳到传导带中 
- Terminology
  - ==Loch / Electron hole / 空穴==
    - Definition
      - 在固体物理学中指共价键中的一些价电子由于热运动获得一些能量，从而摆脱共价键的约束成为自由电子，同时在共价键上留下空位，我们称这些空位为空穴。<br> 由于电子的升迁，在原来是满带的价带中就空出了相等数量的量子态，其余未升迁的电子就可以进入这些量子态而改变自己的量子态。这些空的量子态叫空穴。由于空穴的存在，价带中的电子就松动了，也就可以在电场的作用下形成电流了。
  - ==Dotieren / 掺杂 / Doping==
    - Definition
      - Das Einfügen von Fremdatomen wird Dotieren gennant. Das Dotieren führt zu einer Veränderung der Anzahl an freien Elektronen. <br> 掺杂是半导体制造工艺中，为纯的本质半导体引入杂质，使之电气属性被改变的过程。
    - Glossary
      - ==Donatoren / 施主杂质 / Doner==
        - Definition: Störstellen(杂质) mit einem Valenzband-Elektron mehr als das Halbleiterelement werden als Donatoren bezeichnet. <br> 提供电子载流子的杂质称为施主杂质。相应能级称为施主能级，位于隙带上方靠近导带底附近
        - Entsprechend dotierte Bereiche des Halbleiters werden als ==n-dotiert== bezeichnet. 
        - z.B. 如四价元素锗或硅晶体中掺入五价元素磷、砷、锑等杂质原子时，杂质原子作为晶格的一分子，其五个价电子中有四个与周围的锗（或硅）原子形成共价键，多余的一个电子被束缚于杂质原子附近，这个电子越迁到导带所需能量比从价带激发到导带所需能量小得多，很易激发到导带成为电子载流子，因此**对于掺入施主杂质的半导体，导电载流子主要是被激发到导带中的电子，属电子导电型，称为N型半导体**。由于半导体中总是存在本征激发的电子空穴对，所以**在n型半导体中电子是多数载流子，空穴是少数载流子**。
      - ==Akzeptoren / 受主杂质 / Acceptor== 
        - Definition: 能提供空穴载流子的杂质称为受主(Acceptor)杂质，相应能级称为受主能级，位于带隙下方靠近价带顶附近。
        - Entsprechend dotierte Bereiche des Halbleiters werden als ==p-dotiert== bezeichnet. (半导体中相应的掺杂区域被称为p掺杂。)
        - z.B. 如在锗或硅晶体中掺入微量三价元素硼、铝、镓等杂质原子，由于半导体原子（如硅原子）被杂质原子取代，硼原子外层的三个外层电子与周围的半导体原子形成共价键的时候，会产生一个“空穴”，这个空穴可能吸引束缚电子来“填充”，使得硼原子成为带负电的离子。这样，这类半导体由于含有较高浓度的“空穴”（“相当于”正电荷），成为能够导电的物质。**空穴是多数载流子，杂质半导体主要靠空穴导电，即空穴导电型，称为p型半导体。在P型半导体中空穴是多数载流子，电子是少数载流子。**
      - ==Majoritäts-(Minoritäts-)ladungsträger / 多数(少数)载流子== := P型半导体中空穴浓度较高，为多数载流子(但依旧存在一定的电子作为少数载流子)；n型半导体反之
      
  - ==PN-Übergang / p–n junction / pn结==
    - Definition
      - 采用不同的掺杂工艺，通过扩散作用，将P型半导体与N型半导体制作在同一块半导体（通常是硅或锗）基片上，在它们的交界面形成的空间电荷区称为PN结。 
    - PN结的形成
      - 🚩 Bei gleichem Grad der n- und p- Dotierung, ergibt sich eine sprunghafte Dotierungsdichte; <br> Zunächst sprunghafte Änderung der Ladungsträgerdichte, dann Ausgleich an der Grenzschicht durch Diffusion; <br> Durch Diffusion verbleiben in der n-Zone ortsfeste positive lonen und durch Rekombination der Elektron in der p-Zone ortsfeste negative lonen; <br> Zwischen den positiven lonen in der n-Zone und negativen lonen in der p-Zone entsteht ein elektr. Feld; <br> Wenn Diffusions- und elektr. Feldwirkung auf die freien Ladungsträger gleich ist, führt dies zu einem dynamischen Gleichgewicht 
      - 🚩 在P型半导体和N型半导体结合后，由于N型区内自由电子为多子，空穴几乎为零称为少子，而P型区内空穴为多子，自由电子为少子，在它们的交界处就出现了电子和空穴的浓度差； <br> 由于自由电子和空穴浓度差的原因，有一些电子从N型区向P型区扩散，也有一些空穴要从P型区向N型区扩散。它们扩散的结果就使P区一边失去空穴，留下了带负电的杂质离子，N区一边失去电子，留下了带正电的杂质离子。 <br> 开路中半导体中的离子不能任意移动，因此不参与导电。这些不能移动的带电粒子在P和N区交界面附近，形成了一个==空间电荷区/ Raumsladung /space charge region==，称为PN结。空间电荷区的薄厚和掺杂物浓度有关；<br> 在空间电荷区形成后，由于正负电荷之间的相互作用，**在空间电荷区形成了内电场，其方向是从带正电的N区指向带负电的P区**。显然，这个电场的方向与载流子扩散运动的方向相反，阻止扩散。
    - pn-Übergang mit äußerer Spannung  
      - 要想让PN结导通形成电流，必须消除其空间电荷区的内部电场的阻力 
      - ① P区外接电源负极，N区接正极
        - 相当于内建电场的阻力更大，PN结不能导通，仅有极微弱的反向电流(由少数载流子的漂移运动形成，因少子数量有限，电流饱和）
        - Die Diode ist in Sperrichtung gepolt(极化). Nur Minoritätsträger können als Driftstrom die Sperrschicht durchqueren.   
        - Bei extrem hoher Spannung: ==Zener-Effekt/齐纳击穿==
      - ② P区外接电源正极，N区接负极
        - 可抵消其内部自建电场，使载流子可以继续运动，从而形成线性的正向电流；当反向电压增大至某一数值时，由于少子的数量和能量都增大，会碰撞破坏内部的共价键，使原来被束缚的点子和空穴被释放出来，不断增大电流，最终PN结将被击穿（变为导体）损坏，反向电流急剧增大。
        - 若反向电压>内部电压: alle Majoritätsträger tragen zum Strom bei. Die Diode ist in Durchlassrichtung gepolt.
- ==Gleichrichter / 整流器==
  - Definition
    - Gleichrichter werden zur Umwandlung von Wechselspannung in Gleichspannung verwendet. <br> 整流器是可以将交流电转换成直流电的装置或元件
      - 交流电压 / Wechselspannung：电压的大小和方向都随时间改变的电
      - 直流电压 / Gleichspannung：电压大小和方向不随时间改变就叫直流电，如干电池，蓄电池
    - Beispiel
      - Einweg-Gleichrichter 
        - 交流波形的正半周或负半周其中之一会被消除。只有一半的输入波形会形成输出，对于功率转换是相当没有效率的。 
      - Brücken-Gleichrichter / Diode Bridge / 二极管电桥
        - 用四个或四个以上的二极管组成的电桥电路组态，不论输入电压的电极性是正是负，输出都可以维持相同的极性。
- ==Bipolare Transistoren / 双极性晶体管(俗称三极管)==
  - 二极管的电阻
    - 二极管有正向和反向之分，因此它的两根引脚之间的电阻分为正向电阻和反向电阻两种。
    - 反向电阻要远远大于正向电阻
    - 二极管正向电阻很小；正向电阻的大小和正向电流的大小相关，当二极管的正向电流在变化时，二极管的正向电阻将随之微小变化，正向电流越大，正向电阻越小，反之则越大。   
  - 构成
    - 双极性晶体管由三部分掺杂程度不同的半导体制成。这种晶体管的工作同时涉及电子和空穴两种载流子的流动，因此被称为双极性的。
      - ① 发射极  (E) / Ermitter(由➡️标识)
      - ② 基极(B)/ Basis
        - 物理位置在发射极和集电极之间，它由轻掺杂、高电阻率的材料制成 
      - ③ 集电极(C) / Collector 
  - 类型 <br>电路符号的区别在于发射极所标箭头的指向(指向发射极电流的实际流向) 
    - (常用)NPN型 
      - C与B的电流同时向E流，在发射极汇合之后形成射极电流
    - PNP型 
      - 电流来自于发射极， 分别流向B和C
  - Stromverstärkung Bɴ = ${Iᴄ} \over Iʙ$ 
    - Iᴄ := Kollektorstrom
    - Iʙ := Basisstrom

# Digitale Speicherbausteine
- 时序逻辑电路 / sequential logic circuit
  - Intro
    - 数字电路根据逻辑功能的不同特点，分为组合逻辑电路 & 时序逻辑电路两大类；组合逻辑电路在逻辑功能上的特点是任意时刻的输出仅仅取决于该时刻的输入，与电路原来的状态无关。大部分现实中的电脑电路都是混用组合逻辑与时序逻辑。
  - Definition
    - 指电路任何时刻的稳态输出不仅取决于当前的输入，还与前一时刻输入形成的状态有关。除含有组合电路外，时序电路必须含有存储信息的、有记忆能力的电路，如触发器、寄存器、计数器等。
  - 触发器
    - Definition 
      - 一种具有两种稳态的用于储存的组件，可记录二进制数字信号“1”和“0”。广义触发器的结构均由SR锁存器派生而来。
    - 常见种类
      - ==SR-Latch(set-reset)== <br> realisiert mit NOR-Gattern
        - ① 当S为低电位0，R为高电位1时，输出Q会被强制设置为低电位
        - ② 当S为高电位1，R为低电位时0，输出Q会被强制设置为高电位
        - ③ 当R与S皆为低电位，==回授/Rückkopplung==会让Q与$\bar Q$(Q的反相)保持在一个固定的状态
      - D-Latch (delay)  
        - latch和flip-flop都是时序逻辑，区别为：latch同其所有的输入信号相关，当输入信号变化时latch就变化，没有时钟端；flip-flop受时钟控制，只有在时钟触发时才采样当前的输入，产生输出。
      - D-Flipflops
        - ▷ := flankegesteuerte Eingang； ⏺ := negativ gesteuertes D-Flipflop       
        - steigende Flanke := 信号的一个正缘（rising edge）是数字信号从低电平向高电平的转变。当接入的时脉信号由低电平向高电平转变时，触发器电路被触发.
        - <sub> ¹基本DQCK：复制高CK高位时D的值，其余时刻值保持不变<br> ²基本DQCK⏺：与上相反 <br> ³DQCK▷：只复制CK上升时刻的值 <br> ⁴DQCK▷⏺：与³相反 </sub>
      - JK-Flipflop
        - JK触发器和触发器中最基本的RS触发器结构相似，其区别在于，RS触发器不允许R与S同时为1，而JK触发器允许J与K同时为1。<br>J、K都为0时，Q也为0；J、K相异时，Q与J相同；J、K都为1时，Q = $\overline {Qₙ₋₁}$
        - Die wird immer nur zu dem Zeitpunkt der steigende Flanke ausgewertet.
- Speicherchips Intro
  - If we have *n* bit addresses and *m* bit words, then RAM size will be **2ⁿ**•**m**bit.
  
- Speicher
  - Definition  
    - Bemerkung: In der Informatik wird der Begriff "Speicher" synonym zu Datenspeicher genutzt. Wir betrachten in dieser Veranstaltung nur Halbleiterspeicher / 半导体存储器
    - 半导体存储器是一种用于==数字数据存储==的==数字电路半导体器件==。
      - 如电脑内存，数据会存储在硅集成电路存储芯片上的==金属氧化物半导体(MOS)存储单元==内
  - 半导体存储器分类(wahlfreier Zugriff)
    - 𝟙. 非易失性存储器 / nicht flüchtig / non-volatile memory <br> $\circ$ Definition: 当电流关掉后，所存储的资料不会消失的资料存储设备，重新供电后就能够读取内存资料  <br> $\circ$  Das Eintragen von Informationen in den ROM wird Programmierung (v.s. Speichern beim RAM) gennant. 
      - 依存储器内的资料是否能在使用系统时随时改写为标准分类
        - löschbar
          - EPROM / 可擦可编程只读存储器 / Erasable programmable read only memory  
          - EEPROM / 电可擦可编程只读存储器 / Electrically erasable programmable read only memory 
          - Flash Memory / 闪存
        - nicht löschbar
          - ROM / 只读存储器 / Read-only memory
          - PROM / 可编程只读存储器 / Programmable read-only memory
    - 𝟚. 易失性存储器 / flüchtig /  volatile memory <br> $\circ$ Definition: 当电流中断后，所存储的资料便会消失的电脑存储器
      - RAM(随机存取存储器 /Random Access Memory) <br> Vergleichen mit Read-Only-Memory (ROM) ist RAM schneller.
        - SRAM / 静态随机存取存储器 <br> $\circ$ Definition: 所谓的“静态”，是指这种存储器只要保持通电，里面存储的数据就可以恒常保持 <br> $\circ$ ==CPU的缓存就是SRAM==
          - Verwendung von Flipflops-Latches   
          - SRAMS werden in Bipolar- oder in MOS-Technik hergestellt 
          - ==Auf die Speichergröße ist SRAM teuer, aber sehr schneller (<10ns Zugriffszeit)==
          - Bipolare SRAMS werden wegen ihrer hohen Geschwindigkeit oft als ==Cache-Speicher / 二级高速缓存（Level2 Cache)== der CPU eingesetzt. 
        - DRAM / 动态随机存取存储器 <br> $\circ$ Definition: 利用电容内存储电荷的多少来代表一个二进制比特(bit)是1还是0。由于在现实中晶体管会有漏电电流的现象，导致电容上所存储的电荷数量并不足以正确的判别数据，进而导致数据毁损。<br>$\circ$ 因此对于DRAM来说，周期性地充电是一个不可避免的条件。由于这种需要定时刷新的特性，因此被称为“动态”存储器。 <br>$\circ$ ==电脑的内存条就是DRAM==
          - Pro Speicherzeille 1 Transistor und 1 Kondensator, dadurch hohe Speicherdichte und geringe Kosten
          - langsamer als SRAM(ca. 50ns Zugriffszeit)
          - ==Für den Arbeitsspeicher des Computers wird normalerweise DRAM verwendet.(Verwendung als Hauptspeicher)== 
          - DRAMS sind nur in MOS-Technik realisierbar
          - Aber der Kondensator muss alle 2-5 ms nachgeladen werden, sonst werden die Informationen beim Lesen zerstört.
  
# Mikrokontroller/单片(微型计算)机
- Mikroprocessor / 微处理器
  - Definition
    - 由一片或少数几片大规模集成电路组成的中央处理器。微处理器能完成取指令、执行指令，以及与外界存储器和逻辑部件交换信息等操作，是微型计算机的运算控制部分。它可与存储器和外围电路芯片组成微型计算机。 
    - 特点
      - Kein universelles Gerät
      - Low-end Mikroprozessor + Speicher + I/O + zusätzliche Komponenten (低端微处理器+内存+I/O+附加组件)
      - Kostenoptimierte Steuerungseinheit für bestimmte Anwendungsfelder (针对特定应用领域的成本优化的控制单元)
- Mikrokontroller / MCU
  - Definition
    - 是一种集成电路芯片，是采用超大规模集成电路技术把具有数据处理能力的中央处理器CPU、随机存储器RAM、只读存储器ROM、多种I/O口和中断系统、定时器/计数器等等功能集成到一块硅片上构成的一个小而完善的微型计算机系统，和计算机相比，单片机只缺少了I/O设备。概括的讲：一块芯片就成了一台计算机。它的体积小、质量轻、价格便宜、为学习、应用和开发提供了便利条件 
    - 与CPU比较 
      - I. CPU  
        - ① CPU的运行需要依靠众多的外围器件，比如主板，内存条，硬盘等这些才能组合成一台计算机
        - ② 主流的CPU价格在1000-3000元之间 
        - ③ CPU的频率大多为3-4GHz；功率集中在65-150W；CPU的外置RAM大多为8-32GB；ROM一般多为512GB-2TB的固态硬盘
        - ④ 现代CPU几乎都为64位
      - II. MCU 
        - ① MCU本身就是一台mini版的计算机，它内部集成了中央处理器CPU, RAM, ROM,中断系统，定时器，IO接口等等
        - ② 单片机价格低廉，常用单片机价格为及到几十元不等
        - ③ 单片机的主流频率在8M-72MHz，正常功率约为0.1W，最大功率小于1W；单片机的RAM是内置的，大致在2-256KB之间；内置ROM大小一般在16KB-2MB之间
        - ④ 单片机主要是8位、32位
  - 组成
    - Digitale I/O-Anschlüsse
      - Werden zu Ports von 8 Anschlüssen zusammengefasst (Byte orientierter Zugriff) (被组合成8个连接的端口)
        - bidirektional (d.h. sie können als Ein- und Ausgang genutzt werden)
      - AVR单片机每一个I/O口都对应3个寄存器 
        - DDR / Data Direction Register → Eingang (0) oder Ausgang (1) (即输入输出)
          - Lesen / Schreiben 
          - Legt für jedes Bit des betrachteten Ports fest, ob es ein Ein- oder Ausgangsbit ist (确定所考虑的端口的每个位是输入还是输出位)
        - PORT / Port Register → Ausgabewert（为将内部上拉电阻的状态）
          - Lesen / Schreiben
          - Legt für Ausgangspins fest, ob der Ausgangswert high (1) oder low (0) ist (决定输出引脚的输出值是高（1）还是低（0))
          - Legt für Eingangspins fest, ob Pull-up Widerstände eingeschaltet sind (确定输入引脚的上拉电阻是否被打开)
        - PIN / Port Input Register → Eingabewert (PIN为读取的外部引脚的状态)
          - Nur Lesen
          - Enthält die aktuellen Werte (high oder low) aller Pins (input und output) (包含所有引脚（输入和输出）的电流值（高或低))
    - Interrupts
      - Definition
        - 中断指在计算机运行过程中，当发生某个事件后，CPU会停止当前程序流，转而去处理该事件，并在处理完毕后继续执行原程序流。<br>不同的计算机硬件结构和4er3软件指令不完全相同，因此中断系统也不相同。中断是一种硬件机制，用于通知CPU有个异步事件发生。中断一旦被系统识别，CPU则保存部分（或全部）现场（context），即部分（或全部）寄存器的值，跳转到专门的子程序，称为中断服务程序（ISR - Interrupt Service Routines）。中断服务程序做事件处理，处理完成后执行任务调度，程序回到就绪态优先级最高的任务开始运行(CPU在正常运行的过程中，中断随时可以发生)
        - üblicherweise gibt es
          - ① eine globale Aktivierungsmöglichkeit für alle Interrupts (Global IE)
          - ② eine individuelle Aktivierungsmöglichkeit. 
      - 中断分类
        - 硬中断/Hardware Interrupt
          - 定义
            - 硬中断由外部设备（例如：磁盘，网卡，键盘，时钟）产生，用来通知操作系统外设状态变化(时钟中断：一种硬中断，用于定期打断CPU执行的线程，以便切换给其他线程以得到执行机会)
          - 硬中断的处理流程
            - ① 外设将中断请求发送给中断控制器 ➡ ② 中断控制器根据中断优先级，有序地将中断传递给 CPU ➡ ③ CPU终止执行当前程序流，将CPU所有寄存器的数值保存到栈中 ➡ ④ CPU根据中断向量，从中断向量表中查找中断处理程序的入口地址，执行中断处理程序 ➡ ⑤ CPU恢复寄存器中的数值，返回原程序流停止位置继续执行     
        - 软中断/Software Interrupt  
          - 定义
            - 软中断是一条CPU指令，由当前正在运行的进程产生
          - 软中断的处理流程 
            - ① ②无 ➡ ③ ➡ ④ ➡ ⑤
    - Polling / 轮询
      - Definition 
        - 轮询是一种协议而不是硬件机制，是CPU决策如何提供周边设备服务的方式，又称“程控输入输出”(Programmed I/O)。轮询法的概念是：由CPU定时发出询问，依序询问每一个周边设备是否需要其服务，有即给予服务，服务结束后再问下一个周边，接着不断周而复始 
      - 优缺点
        - 在轮询中，处理器通过重复检查每个设备的命令就绪位来浪费无数的处理器周期   
        - unvereinbar mit Sleep-Mode
        - verlängerte Reaktionszeit
- CPU工作原理
  - CPU内部主要由运算器和控制器组成，就像一条工厂的流水线，内存相当于是工厂的临时仓库，当在电脑上打开一个程序时，和这个程序相关的数据就会从硬盘被传输到内存，这些被临时存储的数据就在内存中等待被CPU提取，而内存中的数据主要是这个程序的数据和指令，数据相当于即将被加工的原材料，而指令就相当于客户的订单，订单上写着对产品的要求。<br>既然内存相当于是仓库，因此CPU工厂自然就有负责在仓库取货的负责人，共有三个：i.)程序计数器：负责通知工厂即将用到的原材料在仓库的具体位置；ii.)地址寄存器：CPU的速度要比内存快很多，主要负责记录正在提取的原材料在内存的具体位置；iii.)数据寄存器：负责整个CPU工厂数据的分发，即从外部进入的及已经生产好的都要经由它来中转。
 
 
  

   