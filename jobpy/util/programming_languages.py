    
def get_programming_languages():   
    
    p_langs = """
    ABAP
    ActionScript
    Ada
    ALGOL
    Alice
    APL
    ASP / ASP.NET
    Assembly Language
    Awk
    BBC Basic
    C
    C++
    C#
    COBOL
    Cascading Style Sheets
    D
    Dart
    Delphi
    Dreamweaver
    Erlang and Elixir
    F#
    Flutter
    FORTH
    FORTRAN
    Functional Programming
    Go
    Haskell
    HTML
    IDL
    INTERCAL
    Java
    Javascript
    jQuery
    LabVIEW
    Lisp
    Logo
    MetaQuotes Language
    ML
    Modula-3
    MS Access
    MySQL
    NXT-G
    Object-Oriented Programming
    Objective-C
    OCaml
    Pascal
    Perl
    PHP
    PL/I
    PL/SQL
    PostgreSQL
    PostScript
    PROLOG
    Pure Data
    Python
    R
    RapidWeaver
    RavenDB
    Rexx
    Ruby on Rails
    S-PLUS
    SAS
    Scala
    Sed
    SGML
    Simula
    Smalltalk
    SMIL
    SNOBOL
    SQL
    SQLite
    SSI
    Stata
    Swift
    Tcl/Tk
    TeX and LaTeX
    Unified Modeling Language
    Unix Shells
    Verilog
    VHDL
    Visual Basic
    Visual FoxPro
    VRML
    WAP/WML
    XML
    XSL"""

    langs = [lang.strip() for lang in p_langs.splitlines() if lang != ""]
    return langs

print(get_programming_languages())
