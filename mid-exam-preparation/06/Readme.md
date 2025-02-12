<center><h1><b>06. Programming Fundamentals Mid Exam Retake</b></h1></center>

[01. Black Flag](#prob1)
[02. Treasure Hunt](#prob2)
[03. Man O War](#prob3)
<ol>
<li><a href="06#prob1">Black Flag</a></li>
<li><a href="prob2">Treasure Hunt</a></li>
<li><a href="prob3">Man O War</a></li>
</ol>


<h1>&nbsp;</h1>
<h1 id="prob1">01. Black Flag</h1>
<p>The problem for exam preparation for the <a href="https://softuni.bg/courses/programming-fundamentals-csharp-java-js-python">Programming Fundamentals Course @SoftUni</a>.</p>
<p>Submit your solutions in the SoftUni judge system at <a href="https://judge.softuni.org/Contests/Practice/Index/1773#0">https://judge.softuni.org/Contests/Practice/Index/1773#0</a>.</p>
<p><em>&nbsp;</em></p>
<p><em>Pirates are invading the sea, and you're tasked to help them plunder</em></p>
<p>Create a program that checks if <strong>target plunder</strong> is <strong>reached</strong>. First, you will receive how many <strong>days</strong> the pirating lasts. Then you will receive how much the pirates <strong>plunder for a day</strong>. Last you will receive the <strong>expected plunder</strong> at the end.</p>
<p>Calculate how much <strong>plunder</strong> the pirates manage to <strong>gather</strong>. Each <strong>day</strong> they gather the <strong>plunder</strong>. Keep in mind that they attack more ships every third day and add additional plunder to their total gain, which is <strong>50% of the daily plunder</strong>. Every <strong>fifth day</strong> the pirates encounter a warship, and after the battle, they <strong>lose 30%</strong> of their <strong>total plunder</strong>.</p>
<p>If the gained plunder is <strong>more or equal</strong> to the target, print the following:</p>
<p><strong>"Ahoy! {totalPlunder} plunder gained."</strong></p>
<p>If the gained plunder is <strong>less</strong> than the target. Calculate the <strong>percentage left</strong> and print the following:</p>
<p><strong>"Collected only {percentage}% of the plunder."</strong></p>
<p>Both numbers should be <strong>formatted</strong> to the <strong>2<sup>nd</sup> decimal place</strong>.</p>
<h2>Input</h2>
<ul>
<li>On the <strong>1<sup>st</sup> line,</strong> you will receive the <strong>days </strong>of the plunder &ndash; an <strong>integer number</strong> in the range <strong>[0&hellip;100000]</strong>.</li>
<li>On the <strong>2<sup>nd</sup> line,</strong> you will receive the <strong>daily plunder</strong> &ndash; an <strong>integer number</strong> in the range <strong>[0&hellip;50]</strong>.</li>
<li>On the <strong>3<sup>rd </sup>line,</strong> you will receive the <strong>expected plunder</strong> &ndash; a <strong>real number</strong> in the range <strong>[0.0&hellip;10000.0]</strong>.</li>
</ul>
<h2>Output</h2>
<ul>
<li>In the end, print whether the plunder <strong>was successful</strong> or <strong>not,</strong> following the format <strong>described above</strong>.</li>
</ul>
<h2 style="text-align: left;">Examples</h2>
<table style="margin-left: auto; margin-right: auto;" width="688">
<tbody>
<tr>
<td width="338">
<p><strong>Input</strong></p>
</td>
<td width="350">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="338">
<p>5<br /> 40<br /> 100</p>
</td>
<td width="350">
<p>Ahoy! 154.00 plunder gained.</p>
</td>
</tr>
<tr>
<td colspan="2" width="688">
<p><strong>Comments</strong></p>
</td>
</tr>
<tr>
<td colspan="2" width="688">
<p>The days are 5, and the daily plunder is 40. On the third day, the total plunder is 120, and since it is a third day, they gain an additional 50% from the daily plunder, which adds up to 140. On the fifth day, the plunder is 220, but they battle with a warship and lose 30% of the collected cargo, and the total becomes 154. That is more than expected.</p>
</td>
</tr>
<tr>
<td width="338">
<p><strong>Input</strong></p>
</td>
<td width="350">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="338">
<p>10</p>
<p>20</p>
<p>380</p>
</td>
<td width="350">
<p>Collected only 36.29% of the plunder.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h1>&nbsp;</h1>
<h1 id="prob2">02. Treasure Hunt</h1>
<p>The problem for exam preparation for the <a href="https://softuni.bg/courses/programming-fundamentals-csharp-java-js-python">Programming Fundamentals Course @SoftUni</a>.</p>
<p>Submit your solutions in the SoftUni judge system at <a href="https://judge.softuni.org/Contests/Practice/Index/1773#1">https://judge.softuni.org/Contests/Practice/Index/1773#1</a>.</p>
<p>&nbsp;</p>
<p><em>The pirates need to carry a treasure chest safely back to the ship, looting along the way.</em></p>
<p>Create a program that <strong>manages</strong> the <strong>state</strong> of the <strong>treasure chest</strong> along the way. On the <strong>first line,</strong> you will receive the <strong>initial loot</strong> of the treasure chest, which is a <strong>string</strong> of <strong>items</strong> separated by a <strong>"|"</strong>.</p>
<p><strong>"{loot<sub>1</sub>}|{loot<sub>2</sub>}|{loot<sub>3</sub>} &hellip; {loot<sub>n</sub>}"</strong></p>
<p>The following lines represent commands <strong>until</strong> <strong>"Yohoho!"</strong> which ends the treasure hunt:</p>
<ul>
<li><strong>"Loot {item<sub>1</sub>} {item<sub>2</sub>}&hellip;{item<sub>n</sub>}"</strong>:
<ul>
<li>Pick up treasure loot along the way. Insert the items at the <strong>beginning</strong> of the chest.</li>
<li>If an item is <strong>already</strong> contained, <strong>don't</strong> insert it.</li>
</ul>
</li>
<li><strong>"Drop {index}"</strong>:
<ul>
<li><strong>Remove</strong> the loot at the given <strong>position</strong> and <strong>add</strong> it at the <strong>end</strong> of the treasure chest.</li>
<li>If the index is <strong>invalid,</strong> skip the command.</li>
</ul>
</li>
<li><strong>"Steal {count}"</strong>:
<ul>
<li>Someone steals the <strong>last count</strong> of loot items. If there are <strong>fewer items</strong> than the given count, <strong>remove as many</strong> as there are.</li>
<li>Print the stolen items separated by <strong>", "</strong>:</li>
</ul>
</li>
</ul>
<p><strong>"{item<sub>1</sub>}, {item<sub>2</sub>}, {item<sub>3</sub>} &hellip; {item<sub>n</sub>}"</strong></p>
<p>In the end, output the <strong>average treasure gain,</strong> which is the <strong>sum</strong> of all treasure items' <strong>length</strong> divided by the <strong>count</strong> of all items inside the chest <strong>formatted</strong> to the <strong>second decimal</strong> point:</p>
<p><strong>"Average treasure gain: {averageGain} pirate credits."</strong></p>
<p>If the chest is <strong>empty,</strong> print the following message:</p>
<p><strong>"Failed treasure hunt."</strong></p>
<h2>Input</h2>
<ul>
<li>On the <strong>1<sup>st</sup> line,</strong> you are going to receive the <strong>initial treasure chest</strong> (<strong>loot</strong> separated by <strong>"|"</strong>).</li>
<li>On the following <strong>lines</strong>, until <strong>"</strong><strong>Yohoho!</strong><strong>"</strong>, you will be receiving commands.</li>
</ul>
<h2>Output</h2>
<ul>
<li>Print the output in the <strong>format</strong> <strong>described</strong> <strong>above</strong>.</li>
</ul>
<h2>Constraints</h2>
<ul>
<li>The <strong>loot items</strong> will be strings containing any ASCII code.</li>
<li>The <strong>indexes</strong> will be integers in the range [<strong>-200</strong>&hellip;<strong>200</strong>]</li>
<li>The <strong>count</strong> will be an integer in the range [<strong>1</strong>&hellip;.<strong>100</strong>]</li>
</ul>
<h2 style="text-align: left;">Examples</h2>
<table style="margin-left: auto; margin-right: auto;" width="688">
<tbody>
<tr style="height: 35px;">
<td style="height: 35px;" width="272">
<p><strong>Input</strong></p>
</td>
<td style="height: 35px;" width="415">
<p><strong>Output</strong></p>
</td>
</tr>
<tr style="height: 155px;">
<td style="height: 155px;" width="272">
<p>Gold|Silver|Bronze|Medallion|Cup</p>
<p>Loot Wood Gold Coins</p>
<p>Loot Silver Pistol</p>
<p>Drop 3</p>
<p>Steal 3</p>
<p>Yohoho!</p>
</td>
<td style="height: 155px;" width="415">
<p>Medallion, Cup, Gold</p>
<p>Average treasure gain: 5.40 pirate credits.</p>
</td>
</tr>
<tr style="height: 35px;">
<td style="height: 35px;" colspan="2" width="688">
<p><strong>Comments</strong></p>
</td>
</tr>
<tr style="height: 229px;">
<td style="height: 229px;" colspan="2" width="688">
<p>The first command <strong>"Loot Wood Gold Coins"</strong> adds <strong>Wood</strong> and <strong>Coins</strong> to the chest but <strong>omits</strong> Gold since it is already contained. The chest now has the following items:</p>
<p><strong>Coins Wood Gold Silver Bronze Medallion Cup</strong></p>
<p>The <strong>second</strong> command adds <strong>only Pistol</strong> to the chest</p>
<p>The <strong>third</strong> command <strong>"</strong><strong>Drop 3</strong><strong>"</strong> removes the <strong>Gold</strong> from the chest, but immediately adds it at the <strong>end</strong>:</p>
<p><strong>Pistol Coins Wood Silver Bronze Medallion Cup Gold</strong></p>
<p>The <strong>fourth</strong> command <strong>"Steal 3" </strong>removes the <strong>last 3</strong> items <strong>Medallion</strong>, <strong>Cup</strong>, <strong>Gold</strong> from the chest and prints them.</p>
<p>In the end calculate the average treasure gain which is the sum of all items length Pistol(<strong>6</strong>) + Coins(<strong>5</strong>) + Wood(<strong>4</strong>)&nbsp; + Silver(<strong>6</strong>) + Bronze(<strong>6</strong>) = <strong>27</strong> and <strong>divide</strong> it by the count 27 / 5 = <strong>5.4</strong> and format it to the <strong>second decimal</strong> point.</p>
<p>&nbsp;</p>
</td>
</tr>
<tr style="height: 35px;">
<td style="height: 35px;" width="272">
<p><strong>Input</strong></p>
</td>
<td style="height: 35px;" width="415">
<p><strong>Output</strong></p>
</td>
</tr>
<tr style="height: 155.2px;">
<td style="height: 155.2px;" width="272">
<p>Diamonds|Silver|Shotgun|Gold</p>
<p>Loot Silver Medals Coal</p>
<p>Drop -1</p>
<p>Drop 1</p>
<p>Steal 6</p>
<p>Yohoho!</p>
</td>
<td style="height: 155.2px;" width="415">
<p>Coal, Diamonds, Silver, Shotgun, Gold, Medals</p>
<p>Failed treasure hunt.</p>
</td>
</tr>
</tbody>
</table>
<h1 style="text-align: center;">&nbsp;</h1>
<h1 style="text-align: center;">&nbsp;</h1>
<h1>&nbsp;</h1>
<h1 id="prob3">03. Man O War</h1>
<p>The problem for exam preparation for the <a href="https://softuni.bg/courses/programming-fundamentals-csharp-java-js-python">Programming Fundamentals Course @SoftUni</a>.</p>
<p>Submit your solutions in the SoftUni judge system at <a href="https://judge.softuni.org/Contests/Practice/Index/1773#2">https://judge.softuni.org/Contests/Practice/Index/1773#2</a>.</p>
<p>&nbsp;</p>
<p><em>The pirates encounter a huge Man-O-War at sea. </em></p>
<p>Create a program that <strong>tracks</strong> the <strong>battle</strong> and either chooses a <strong>winner</strong> or prints a <strong>stalemate</strong>. On the <strong>first line,</strong> you will receive the <strong>status</strong> of the <strong>pirate ship</strong>, which is a <strong>string</strong> representing <strong>integer sections</strong> separated by <strong>"&gt;"</strong>. On <strong>the second line,</strong> you will receive the <strong>same</strong> type of status, but for the <strong>warship</strong>:</p>
<p><strong>"{section<sub>1</sub>}&gt;{section<sub>2</sub>}&gt;{section<sub>3</sub>}&hellip; {section<sub>n</sub>}"</strong></p>
<p>On the <strong>third line,</strong> you will receive the <strong>maximum health capacity</strong> a section of the ship can reach.</p>
<p>The following lines represent commands <strong>until</strong> <strong>"Retire"</strong>:</p>
<ul>
<li><strong>"Fire {index} {damage}"</strong> - the pirate ship <strong>attacks</strong> the warship with the <strong>given damage</strong> at that section. Check if the <strong>index is valid</strong> and if not, <strong>skip</strong> the command. If the section <strong>breaks</strong> (health &lt;= 0) the warship <strong>sinks</strong>, print the following and <strong>stop</strong> the program: <strong>"You won! The enemy ship has sunken."</strong></li>
<li><strong>"Defend {startIndex} {endIndex} {damage}"</strong> - the warship <strong>attacks</strong> the pirate ship with the <strong>given damage</strong> at that <strong>range</strong> (<strong>indexes are inclusive)</strong>. Check if both <strong>indexes are valid</strong> and if not, <strong>skip</strong> the command. If the section <strong>breaks</strong> (health &lt;= 0) the pirate ship <strong>sinks</strong>, print the following and <strong>stop</strong> the program:</li>
</ul>
<p><strong>"You lost! The pirate ship has sunken."</strong></p>
<ul>
<li><strong>"Repair {index} {health}"</strong> - the crew <strong>repairs</strong> a section of the <strong>pirate ship</strong> with the <strong>given health</strong>. Check if the <strong>index is valid</strong> and if not, <strong>skip</strong> the command. The health of the section <strong>cannot</strong> exceed the <strong>maximum health capacity</strong>.</li>
<li><strong>"Status"</strong> - prints the <strong>count</strong> of all sections of the <strong>pirate ship</strong> that need repair soon, which are all sections that are <strong>lower than 20%</strong> of the <strong>maximum</strong> <strong>health capacity</strong>. Print the following:</li>
</ul>
<p><strong>"{count} sections need repair."</strong></p>
<p>In the end, if a <strong>stalemate</strong> occurs, print the <strong>status</strong> of <strong>both</strong> ships, which is the <strong>sum</strong> of their individual sections, in the following format:</p>
<p><strong>"Pirate ship status: {pirateShipSum}</strong></p>
<p><strong>Warship status: {warshipSum}"</strong></p>
<h2>Input</h2>
<ul>
<li>On the <strong>1<sup>st</sup> line,</strong> you are going to receive the <strong>status</strong> of the <strong>pirate ship</strong> (<strong>integers</strong> separated by <strong>'&gt;'</strong>).</li>
<li>On the <strong>2<sup>nd</sup> line,</strong> you are going to receive the <strong>status</strong> of the</li>
<li>On the <strong>3<sup>rd</sup> line,</strong> you will receive the <strong>maximum health</strong> a section of a ship can reach.</li>
<li>On the following <strong>lines</strong>, until <strong>"</strong><strong>Retire</strong><strong>"</strong>, you will be receiving commands.</li>
</ul>
<h2>Output</h2>
<ul>
<li>Print the output in the <strong>format</strong> <strong>described</strong> <strong>above</strong>.</li>
</ul>
<h2>Constraints</h2>
<ul>
<li>The <strong>section numbers</strong> will be integers in the range [<strong>1</strong>&hellip;.<strong>1000</strong>].</li>
<li>The <strong>indexes</strong> will be integers [<strong>-200</strong>&hellip;.<strong>200</strong>].</li>
<li>The <strong>damage</strong> will be an integer in the range [<strong>1</strong>&hellip;.<strong>1000</strong>].</li>
<li>The <strong>health</strong> will be an integer in the range [<strong>1</strong>&hellip;.<strong>1000</strong>].</li>
</ul>
<h2>Examples</h2>
<table style="margin-left: auto; margin-right: auto;" width="688">
<tbody>
<tr>
<td width="338">
<p><strong>Input</strong></p>
</td>
<td colspan="2" width="350">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="338">
<p>12&gt;13&gt;11&gt;20&gt;66</p>
<p>12&gt;22&gt;33&gt;44&gt;55&gt;32&gt;18</p>
<p>70</p>
<p>Fire 2 11</p>
<p>Fire 8 100</p>
<p>Defend 3 6 11</p>
<p>Defend 0 3 5</p>
<p>Repair 1 33</p>
<p>Status</p>
<p>Retire</p>
</td>
<td colspan="2" width="350">
<p>2 sections need repair.</p>
<p>Pirate ship status: 135</p>
<p>Warship status: 205</p>
</td>
</tr>
<tr>
<td colspan="3" width="688">
<p><strong>Comments</strong></p>
</td>
</tr>
<tr>
<td colspan="3" width="688">
<p>First, we receive the command "<strong>Fire 2 11</strong>", and damage the warship at section index 2, which is currently 33, and after reduction, the status of the warship is the following:</p>
<p><strong>12 22 22 44 55 32 18</strong></p>
<p>The <strong>second</strong> and <strong>third</strong> commands have <strong>invalid indexes</strong>, so we skip them.</p>
<p>The <strong>fourth</strong> command, <strong>"</strong><strong>Defend 0 3 5</strong><strong>" </strong>damages <strong>4 sections</strong> of the pirate ship with <strong>5,</strong> which results in the following states:</p>
<p><strong>7 8 6 15 66</strong></p>
<p>The <strong>fifth</strong> command, <strong>"</strong><strong>Repair 1 33</strong><strong>" </strong>repairs the pirate ship section and adds <strong>33 health</strong> to the current <strong>8,</strong> which results in <strong>41</strong></p>
<p>Only <strong>2 sections</strong> of the pirate ship (<strong>7</strong> and <strong>6</strong>) need repair soon.</p>
<p>In the end, there is a <strong>stalemate,</strong> so we print both ship statuses (<strong>sum</strong> of all sections).</p>
<p>&nbsp;</p>
</td>
</tr>
<tr>
<td colspan="2" width="344">
<p><strong>Input</strong></p>
</td>
<td width="344">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="338">
<p>2&gt;3&gt;4&gt;5&gt;2</p>
<p>6&gt;7&gt;8&gt;9&gt;10&gt;11</p>
<p>20</p>
<p>Status</p>
<p>Fire 2 3</p>
<p>Defend 0 4 11</p>
<p>Repair 3 18</p>
<p>Retire</p>
</td>
<td colspan="2" width="350">
<p>3 sections need repair.</p>
<p>You lost! The pirate ship has sunken.</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
