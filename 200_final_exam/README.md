<h1 style="text-align: center;"><strong>💯 Regular Final Practical Exam</strong></h1>
<p>&nbsp;</p>

<h3><strong>Problems:</strong></h3>

[01. String Manipulator](#1)<br/>
[02. Message Translator](#2)<br/>
[03. Followers](#3)<br/>


<h1 id ="1">📝 Problem 1 &ndash; String Manipulator</h1>


<p>Create a program that executes changes over a string. First, you are going to <strong>receive</strong> <strong>the string</strong>, then commands.</p>
<p>You will be receiving <strong>commands</strong> until the <strong>"End"</strong> command. There are <strong>six</strong> possible commands:</p>
<ul>
<li><strong>"Translate {char} {replacement}"</strong>
<ul>
<li><strong>Replace</strong> all occurrences of the <strong>given char</strong> with the <strong>given replacement</strong>, then <strong>print</strong> the <strong>string</strong>.</li>
</ul>
</li>
<li>"<strong>Includes {substring}"</strong>
<ul>
<li><strong>Check</strong> if the current string <strong>includes the given substring </strong>and <strong>print</strong> <strong>"True"</strong> or <strong>"False"</strong>.</li>
</ul>
</li>
<li>"<strong>Start {substring}"</strong>
<ul>
<li><strong>Check</strong> if the current string <strong>starts</strong> with the <strong>given substring</strong> and <strong>print</strong> <strong>"True"</strong> or <strong>"False"</strong>.</li>
</ul>
</li>
<li>"<strong>Lowercase"</strong>
<ul>
<li>Make the <strong>whole</strong> <strong>string</strong> <strong>lowercased</strong>, then <strong>print</strong></li>
</ul>
</li>
<li>"<strong>FindIndex {char}"</strong>
<ul>
<li>Find the <strong>index of the last occurrence of the given char</strong>, then <strong>print</strong></li>
</ul>
</li>
<li>"<strong>Remove {startIndex} {count}"</strong>
<ul>
<li>Remove the <strong>given count of characters</strong> from the string, starting from the<strong> start index</strong>, then <strong>print</strong></li>
</ul>
</li>
</ul>
<h2>Input</h2>
<ul>
<li>On the <strong>first line,</strong> you are going to receive the <strong>string</strong>.</li>
<li>On the following <strong>lines</strong>, until the <strong>"End"</strong> command is received, you will be receiving commands.</li>
<li>All commands are case-<strong>sensitive</strong>.</li>
<li>The <strong>input</strong> will <strong>always</strong> be <strong>valid</strong>.</li>
</ul>
<h2>Output</h2>
<ul>
<li><strong>Print</strong> the <strong>output</strong> of every <strong>command</strong> in the <strong>format</strong> <strong>described</strong> <strong>above</strong>.</li>
</ul>
<h2>Examples</h2>
<table width="688">
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
<p>//Thi5 I5 MY 5trING!//<br /> Translate 5 s<br /> Includes string<br /> Start //This<br /> Lowercase<br /> FindIndex i<br /> Remove 0 10<br /> End</p>
</td>
<td width="350">
<p>//This Is MY strING!//</p>
<p>False</p>
<p>True</p>
<p>//this is my string!//</p>
<p>16</p>
<p>my string!//</p>
</td>
</tr>
<tr>
<td width="338">
<p>*S0ftUni is the B3St Plac3**</p>
<p>Translate 2 o</p>
<p>Includes best</p>
<p>Start the</p>
<p>Lowercase</p>
<p>FindIndex p</p>
<p>Remove 2 7</p>
<p>End</p>
</td>
<td width="350">
<p>*S0ftUni is the B3St Plac3**</p>
<p>False</p>
<p>False</p>
<p>*s0ftuni is the b3st plac3**</p>
<p>21</p>
<p>*sis the b3st plac3**</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

<h1 id = "2">🗣️ Problem 2 - Message Translator</h1>


<p>Create a program that <strong>checks</strong> if <strong>inputs</strong> have a <strong>valid command and string</strong> and <strong>translates</strong> it. You will receive <strong>n</strong> count of strings. For each string, check if it's valid.</p>
<p>A string is <strong>valid</strong> when:</p>
<ul>
<li>The command is <strong>surrounded by</strong> <strong>"</strong><strong>!</strong><strong>"</strong>, <strong>starts</strong> with an <strong>uppercase</strong> letter, <strong>followed</strong> <strong>only</strong> by <strong>lowercase</strong></li>
<li>The command Is <strong>minimum 3 characters long</strong></li>
<li>There is a <strong>colon</strong> after the command.</li>
<li>There is a string <strong>consisting of alphabetical</strong> <strong>letters </strong>between square brackets <strong>"</strong><strong>[</strong><strong>" </strong>and <strong>"</strong><strong>]</strong><strong>"</strong>.</li>
<li>It must be <strong>minimum 8</strong> characters long.</li>
</ul>
<p><strong>Example for a valid string</strong><strong>:</strong></p>
<p><strong>"!Send!:[IvanisHere]"</strong></p>
<p>You must <strong>check</strong> if the <strong>string</strong> is <strong>valid</strong> and if it <strong>is</strong> - <strong>translates</strong> it. If it <strong>isn't </strong>- <strong>print</strong> the following <strong>message</strong>:</p>
<p><strong>"The message is invalid"</strong></p>
<p><strong>Translating</strong> a <strong>string</strong> means taking <strong>all</strong> <strong>letters</strong> from the string and <strong>turn</strong> them <strong>into</strong> <strong>ASCII</strong> <strong>numbers</strong>. After successful translation, print it in the following format:</p>
<p><strong>"{command}:{</strong><strong>number1</strong><strong>} {number2} &hellip; {numberN}"</strong></p>
<p><strong>Note: Translate only the text in the string</strong><strong>. If you have </strong><strong>"[Ivan is Here]"</strong><strong>, the part that you need to translate is </strong><strong>"Ivan is Here"</strong><strong>. </strong></p>
<h2>Input</h2>
<ul>
<li>On the <strong>first</strong> line, you will receive an integer <strong>n</strong> - the count of inputs.</li>
<li>On the next <strong>n </strong>lines - <strong>input</strong> that you must <strong>check</strong> if it has a <strong>valid</strong> <strong>string</strong>.</li>
</ul>
<h2>Output</h2>
<ul>
<li>Print the result in format described above.</li>
</ul>
<h2>Examples</h2>
<table width="595">
<tbody>
<tr>
<td width="227">
<p><strong>Input</strong></p>
</td>
<td width="369">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="227">
<p>2</p>
<p>!Send!:[IvanisHere]</p>
<p>*Time@:[Itis5amAlready]</p>
</td>
<td width="369">
<p>Send: 73 118 97 110 105 115 72 101 114 101</p>
<p>The message is invalid</p>
</td>
</tr>
<tr>
<td width="227">
<p>3</p>
<p>go:[outside]</p>
<p>!drive!:YourCarToACarWash</p>
<p>!Watch!:[LordofTheRings]</p>
</td>
<td width="369">
<p>The message is invalid</p>
<p>The message is invalid</p>
<p>Watch: 76 111 114 100 111 102 84 104 101 82 105 110 103 115</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>

<h1 id="3">🔔 Problem 3 - Followers</h1>


<p>Create a program that keeps the information about Jane's Facebook <strong>followers</strong>, their <strong>likes</strong>, and <strong>comments.</strong> Keep a record of the followers, each with the count of likes and comments Jane has received from them.</p>
<p>You will be receiving <strong>lines</strong> with commands until you receive the <strong>"</strong><strong>Log out"</strong> command. There are four <strong>possible</strong> commands:</p>
<ul>
<li><strong>"New follower: {username}"</strong>:
<ul>
<li><strong>Add</strong> the <strong>username</strong> to your <strong>records </strong>(with 0 likes and 0 comments).</li>
<li>If a person with the given <strong>username</strong> already <strong>exists, ignore</strong> <strong>the line</strong>.</li>
</ul>
</li>
<li><strong>"Like: {username}: {count}"</strong>:
<ul>
<li>If the username <strong>doesn't</strong> exist, <strong>add</strong> it to your records with the given count of likes.</li>
<li>If the username <strong>exists</strong>, <strong>increase</strong> the count of likes with the given count.</li>
</ul>
</li>
<li><strong>"Comment: </strong><strong>{username}</strong><strong>"</strong>:
<ul>
<li>If the username <strong>doesn't</strong> exist, <strong>add</strong> it to your records with <strong>1 comment</strong>.</li>
<li>If the username <strong>exists</strong>, <strong>increase</strong> the count of comments with <strong>1</strong>.</li>
</ul>
</li>
<li><strong>"Blocked: </strong><strong>{username}</strong><strong>"</strong>:
<ul>
<li><strong>Delete </strong>all records of the given username.</li>
<li>If it doesn't exist, print: <strong>"{Username} doesn't"</strong></li>
</ul>
</li>
</ul>
<p>In the end, you have to <strong>print the count of followers, each follower </strong>with their <strong>likes and comments</strong> (the <strong>sum</strong> of <strong>likes</strong> and <strong>comments</strong>):</p>
<p><strong>"{count} followers"</strong></p>
<p><strong>{username}: {likes+comments}</strong></p>
<p><strong>{username}: {likes+comments}</strong></p>
<p><strong>&hellip;</strong></p>
<p><strong>{username}: {likes+comments}"</strong></p>
<h2>Input</h2>
<ul>
<li>You will be receiving lines until you receive the <strong>"</strong><strong>Log out"</strong></li>
<li>The input will <strong>always</strong> be <strong>valid</strong>.</li>
</ul>
<h2>Output</h2>
<ul>
<li>Print the users with their <strong>likes</strong> in the <strong>format</strong> described above.</li>
</ul>
<h2>Examples</h2>
<table width="643">
<tbody>
<tr>
<td width="312">
<p><strong>Input</strong></p>
</td>
<td width="331">
<p><strong>Output</strong></p>
</td>
</tr>
<tr>
<td width="312">
<p>New follower: George</p>
<p>Like: George: 5</p>
<p>New follower: George</p>
<p>Log out</p>
</td>
<td width="331">
<p>1 followers</p>
<p>George: 5</p>
</td>
</tr>
<tr>
<td width="312">
<p>Like: Katy: 3</p>
<p>Comment: Katy</p>
<p>New follower: Bob</p>
<p>Blocked: Bob</p>
<p>New follower: Amy</p>
<p>Like: Amy: 4</p>
<p>Log out</p>
</td>
<td width="331">
<p>2 followers</p>
<p>Katy: 4</p>
<p>Amy: 4</p>
</td>
</tr>
<tr>
<td width="312">
<p>Blocked: Amy</p>
<p>Comment: Amy</p>
<p>New follower: Amy</p>
<p>Like: Tom: 5</p>
<p>Like: Ellie: 5</p>
<p>Log out</p>
</td>
<td width="331">
<p>Amy doesn't exist.</p>
<p>3 followers</p>
<p>Amy: 1</p>
<p>Tom: 5</p>
<p>Ellie: 5</p>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
