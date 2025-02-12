<h1>Problem 3 - Man-O-War</h1>
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
