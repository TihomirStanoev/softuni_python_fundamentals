<h1 style="text-align: center;"><strong>💯 Regular Mid Practical Exam</strong></h1>
<p>&nbsp;</p>


<h3><strong>Problems:</strong></h3>

[01. Burger Bus](#1)<br/>
[02. Numbers](#2)<br/>
[03. Deck of Cards](#3)<br/>




<h1 id = "1">🍔 Problem 1 - Burger Bus</h1>
<p><em>The Burger Bus travels around the country and serves delicious burgers. You need to help the owner keep track of his</em></p>
<p><em>income and expenses along the way.</em></p>
<p><strong>First</strong>, you will receive the <strong>number of cities</strong> the bus has visited. Then for <strong>every city,</strong> you will receive:</p>
<ul>
<li><strong>the</strong> <strong>name of the city</strong></li>
<li><strong>how much money the owner earned</strong></li>
<li><strong>owner's expenses</strong></li>
</ul>
<p>Every <strong>3<sup>rd</sup> (third)</strong> city the bus visits, the owner <strong>organizes a special event</strong> to ensure a true "Burger Bus" experience, spending<strong> an additional 50% over costs</strong>.</p>
<p>In every <strong>5<sup>th</sup> (fifth)</strong> city, it is <strong>raining,</strong> and the owner <strong>losses 10% of the money</strong> he earned. In a rainy city, there is <strong>no possibility to organize a special event</strong>.</p>
<p>You have to calculate the owner's <strong>profit for each city</strong> and his <strong>total profit from the tour</strong>. Profit is calculated by <strong>deducting</strong> the <strong>expenses</strong> from the <strong>income</strong>.</p>
<h3>Input</h3>
<p>The input will consist of:</p>
<ul>
<li><strong>Number</strong> of cities &ndash; <strong>integer </strong>in the range [1&hellip;15]</li>
<li>For each city, you will receive the following information:
<ul>
<li><strong>name of the city </strong>-<strong> string</strong></li>
<li><strong>owner's </strong><strong>income</strong> - a <strong>real number</strong> in the range [0.0&hellip;10 000.0]</li>
<li><strong>owner's </strong><strong>expenses</strong> - a <strong>real number</strong> in the range [0.0&hellip;10 000.0]</li>
</ul>
</li>
<li>The input will always be in the correct format.</li>
</ul>
<h3>Output</h3>
<ul>
<li>For every city, you need to print the following message:</li>
</ul>
<p>"In {cityName} Burger Bus earned {profit} leva."</p>
<ul>
<li>At the end of the tour, print:</li>
</ul>
<p>"Burger Bus total profit: {totalProfit} leva."</p>
<p><strong>NOTE: The profit and the total profit should be formatted</strong> to <strong>the 2nd</strong> decimal place.</p>
<h3>Examples</h3>
<table width="696">
<tbody>
<tr>
<td width="198">
<p><strong>Input</strong></p>
</td>
<td width="498">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="198">
<p>3</p>
<p>Sofia</p>
<p>895.67</p>
<p>213.50</p>
<p>Plovdiv</p>
<p>2563.20</p>
<p>890.26</p>
<p>Burgas</p>
<p>2360.55</p>
<p>600.00</p>
</td>
<td width="498">
<p>In Sofia Burger Bus earned 682.17 leva.</p>
<p>In Plovdiv Burger Bus earned 1672.94 leva.</p>
<p>In Burgas Burger Bus earned 1460.55 leva.</p>
<p>Burger Bus total profit: 3815.66 leva.</p>
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td width="198">
<p><strong>Input</strong></p>
</td>
<td width="498">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="198">
<p>5</p>
<p>Lille</p>
<p>2226.00</p>
<p>1200.60</p>
<p>Rennes</p>
<p>6320.60</p>
<p>5460.20</p>
<p>Reims</p>
<p>600.20</p>
<p>452.32</p>
<p>Bordeaux</p>
<p>6925.30</p>
<p>2650.40</p>
<p>Montpellier</p>
<p>680.50</p>
<p>290.20</p>
</td>
<td width="498">
<p>In Lille Burger Bus earned 1025.40 leva.</p>
<p>In Rennes Burger Bus earned 860.40 leva.</p>
<p>In Reims Burger Bus earned -78.28 leva.</p>
<p>In Bordeaux Burger Bus earned 4274.90 leva.</p>
<p>In Montpellier Burger Bus earned 322.25 leva.</p>
<p>Burger Bus total profit: 6404.67 leva.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1 id = "2">🔢Problem 2 - Numbers</h1>
<p>You are given <strong>numbers</strong> in <strong>a sequence on a single line, separated by a space</strong>. After that, you will receive <strong>commands</strong> that modify the sequence differently:</p>
<ul>
<li><strong>"Add {value}"</strong> - you should <strong>add</strong> the given value to <strong>the end</strong> of the sequence.</li>
<li><strong>"Remove {value}"</strong> - you should <strong>remove</strong> the <strong>first occurrence</strong> of the given value if there is such.</li>
<li><strong>"Replace {value} {replacement}"</strong> - you should <strong>replace</strong> the <strong>first occurrence</strong> of the <strong>given value</strong> with the <strong>replacement </strong>if there is such occurrence.</li>
<li><strong>"Collapse {value}"</strong> you must <strong>remove each number with a value less</strong> than the given one.</li>
</ul>
<p>When you receive the command <strong>"Finish"</strong>, you should <strong>print the modified sequence</strong> and end the program.</p>
<h3>Input / Constraints</h3>
<ul>
<li>On the first line, you will receive a sequence with numbers, separated by spaces - integers in the range</li>
</ul>
<p><strong>[-1000&hellip;1000]</strong><strong>.</strong></p>
<ul>
<li>On the following lines, you will receive commands until the <strong>"Finish"</strong> command is received.</li>
<li>The commands will always be valid.</li>
</ul>
<h3>Output</h3>
<ul>
<li>Print a single line the array of numbers separated by a space, with the modified values.</li>
</ul>
<h3>Examples</h3>
<table width="624">
<tbody>
<tr>
<td width="274">
<p><strong>Input</strong></p>
</td>
<td width="350">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="274">
<p>1 4 5 19</p>
<p>Add 1</p>
<p>Remove 4</p>
<p>Finish</p>
</td>
<td width="350">
<p>1 5 19 1</p>
</td>
</tr>
<tr>
<td width="274">
<p>1 20 -1 10</p>
<p>Collapse 8</p>
<p>Finish</p>
</td>
<td width="350">
<p>20 10</p>
</td>
</tr>
<tr>
<td width="274">
<p>5 9 70 -56 9 9</p>
<p>Replace 9 10</p>
<p>Remove 9</p>
<p>Finish</p>
</td>
<td width="350">
<p>5 10 70 -56 9</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1 id = "3">🃏Problem 3 - Deck of Cards</h1>
<p>You will <strong>receive a list</strong> of Cards <strong>on a single line separated by </strong><strong>", "</strong><strong>.</strong> On the <strong>next line,</strong> you will receive a number <strong>n</strong>. On the next <strong>n</strong> lines, you will receive commands that could be:</p>
<ul>
<li><strong>"Add, {CardName}"</strong>:
<ul>
<li><strong>Add </strong>the given <strong>card</strong> to the card deck and <strong>print</strong>: <strong>"Card successfully added"</strong></li>
</ul>
</li>
<li>If it is <strong>already in the deck</strong>, print: <strong>"Card is already in the deck"</strong></li>
<li><strong>"Remove, {CardName}"</strong>:
<ul>
<li><strong>Remove the given card</strong> from the card deck and print<strong>: </strong><strong>"Card successfully removed"</strong></li>
<li>If it is <strong>not</strong> <strong>in the deck</strong>, print: <strong>"Card not found"</strong></li>
</ul>
</li>
<li><strong>"Remove At, {index}"</strong>:</li>
<li><strong>Remove</strong> <strong>the card</strong> at the given index and <strong>print</strong>: <strong>"</strong><strong>Card successfully removed</strong><strong>"</strong></li>
<li>If the <strong>index is not in the range</strong> of the list, print:<strong> "</strong><strong>Index out of range</strong><strong>"</strong></li>
<li>"<strong>Insert, {index}, {CardName}"</strong>:
<ul>
<li><strong>Add the card at the given index</strong> and <strong>print: "</strong><strong>Card successfully added</strong><strong>"</strong></li>
</ul>
</li>
<li>If the <strong>index is out of range</strong>, <strong>print: "</strong><strong>Index out of range</strong><strong>"</strong></li>
<li>If the <strong>index is in range, </strong>but the <strong>card is already in the deck</strong>, <strong>print: "</strong><strong>Card is already added</strong><strong>"</strong></li>
</ul>
<h4>Input</h4>
<ul>
<li>The <strong>first input line</strong> will contain the <strong>list</strong> of</li>
<li>The <strong>second</strong> <strong>input </strong>will be the<strong> number of commands</strong> &ndash; an <strong>integer number</strong> in the range [0&hellip;50].</li>
<li>On the <strong>following input lines,</strong> you will be receiving commands.</li>
</ul>
<h4>Output</h4>
<ul>
<li>After going through all the commands, you need to <strong>print </strong>all cards <strong>on a single line separated by </strong><strong>", "</strong>.</li>
</ul>
<h4>Examples</h4>
<table width="716">
<tbody>
<tr>
<td width="272">
<p><strong>Input</strong></p>
</td>
<td width="444">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="272">
<p>Ace of Diamonds, Queen of Hearts, King of Clubs</p>
<p>3</p>
<p>Add, King of Diamonds</p>
<p>Insert, 2, Jack of Spades</p>
<p>Remove, Ace of Diamonds</p>
</td>
<td width="444">
<p>Card successfully added</p>
<p>Card successfully added</p>
<p>Card successfully removed</p>
<p>Queen of Hearts, Jack of Spades, King of Clubs, King of Diamonds</p>
</td>
</tr>
<tr>
<td width="272">
<p>Two of Clubs, King of Spades, Five of Spades, Jack of Hearts</p>
<p>2</p>
<p>Add, Two of Clubs</p>
<p>Remove, Five of Hearts</p>
</td>
<td width="444">
<p>Card is already in the deck</p>
<p>Card not found</p>
<p>Two of Clubs, King of Spades, Five of Spades, Jack of Hearts</p>
</td>
</tr>
<tr>
<td width="272">
<p>Jack of Spades, Ace of Clubs, Jack of Clubs</p>
<p>2</p>
<p>Insert, -1, Queen of Spades</p>
<p>Remove At, 1</p>
</td>
<td width="444">
<p>Index out of range</p>
<p>Card successfully removed</p>
<p>Jack of Spades, Jack of Clubs</p>
</td>
</tr>
</tbody>
</table>
