# revision 32608
# category Package
# catalog-ctan /macros/latex/contrib/esami
# catalog-date 2014-01-07 23:48:24 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-esami
Version:	1.1
Release:	1
Summary:	Typeset exams with scrambled questions and answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esami
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esami.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esami.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to typeset exams with multiple
choice, open questions and many other types of exercise. Both
questions and answers may be randomly distributed within the
exam, and the solutions are typeset automatically. Exercises
may contain a wide number of random parameters and it is
possible to do arithmetical operations on them. The package is
localised in Italian, English, French, German, Greek and
Spanish.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/esami/es-UKenglish.lng
%{_texmfdistdir}/tex/latex/esami/es-USenglish.lng
%{_texmfdistdir}/tex/latex/esami/es-french.lng
%{_texmfdistdir}/tex/latex/esami/es-german.lng
%{_texmfdistdir}/tex/latex/esami/es-greek.lng
%{_texmfdistdir}/tex/latex/esami/es-italian.lng
%{_texmfdistdir}/tex/latex/esami/es-spanish.lng
%{_texmfdistdir}/tex/latex/esami/esami.sty
%doc %{_texmfdistdir}/doc/latex/esami/README
%doc %{_texmfdistdir}/doc/latex/esami/doc/esami-doc-en.pdf
%doc %{_texmfdistdir}/doc/latex/esami/doc/esami-doc-en.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/esami-doc-it.dtx
%doc %{_texmfdistdir}/doc/latex/esami/doc/esami-doc-it.pdf
%doc %{_texmfdistdir}/doc/latex/esami/doc/esami-doc-it.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/esami.bib
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/esami-xyz.cfg
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/master-sol.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/master.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/problem1.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/problem2-tabella.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/problem3-matching.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/problem4-fillin.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test1.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test11.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test12.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test13.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test14.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test2.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test3.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test4.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/test5-fillin.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/testA-sol.pdf
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/testA.pdf
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/testA.tex
%doc %{_texmfdistdir}/doc/latex/esami/doc/examples/totale-versioni.tex
%doc %{_texmfdistdir}/doc/latex/esami/esami-xyz.cfg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
