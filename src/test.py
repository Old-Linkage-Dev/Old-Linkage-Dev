
from .OLD import TEL as TEL;
from .OLD import CLI as CLI;

line = "你好Hello";
cmage = [
    "#$%",
    "$%^",
    "%^.",
];


el = CLI.ElemLabel(value = line, boxstyle = '=', colorstyle = CLI.STYLE_BLACKWHITE);
el.y = 4;
el.x = 50;

ec = CLI.ElemCmage(value = cmage, boxstyle = '=', colorstyle = CLI.STYLE_BLACKWHITE);
ec.y = 6;
ec.x = 10;

_s = '';
for elm in [el, ec]:
    elm.update('');
    _s += elm.draw(1, 1, 30, 80, False);

print(_s);
print();
