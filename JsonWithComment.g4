// Derived from http://json.org
grammar JsonWithComment;

json:   obj
    |   array
    ;

obj
    :   '{' pair (',' pair)* ','? '}'    # AnObject
    |   '{' '}'                     # EmptyObject
    ;
	
array
    :   '[' value (',' value)* ','? ']'  # ArrayOfValues
    |   '[' ']'                     # EmptyArray
    ;

pair:   STRING ':' value ;

value
    :   STRING		# String
    |   NUMBER		# Atom
    |   obj     	# ObjectValue
    |   array  		# ArrayValue
    |   'true'		# Atom
    |   'false'		# Atom
    |   'null'		# Atom
    ;

LCURLY : '{' ;
LBRACK : '[' ;
STRING : STRING_single | STRING_double | STRING_back ;


fragment STRING_double :  '"' (ESC_double | ~["\\])* '"' ;
fragment ESC_double :   '\\' (["\\/bfnrt] | UNICODE) ;

fragment STRING_single :  '\'' (ESC_single | ~['\\])* '\'' ;
fragment ESC_single :   '\\' (['\\/bfnrt] | UNICODE) ;

fragment STRING_back :  '`' (ESC_back | ~[`\\])* '`' ;
fragment ESC_back :   '\\' ([`\\/bfnrt] | UNICODE) ;


fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;

NUMBER
    :   '-'? INT '.' INT EXP?   // 1.35, 1.35E-9, 0.3, -4.5
    |   '-'? INT EXP            // 1e10 -3e4
    |   '-'? INT                // -3, 45
    ;
fragment INT :   '0' | '1'..'9' '0'..'9'* ; // no leading zeros
fragment EXP :   [Ee] [+\-]? INT ; // \- since - means "range" inside [...]

WhiteSpace
    :   [ \t]+ -> skip
    ;

Newline
    :   ('\r' '\n'?| '\n') -> skip
    ;

BlockComment
    :   '/*' .*? '*/' -> skip
    ;

CLineComment
    :   '//' ~[\r\n]* -> skip
    ;

PyLineComment
    :   '#' ~[\r\n]* -> skip
    ;