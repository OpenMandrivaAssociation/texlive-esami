%global tl_name esami
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Typeset exams with scrambled questions and answers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esami
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esami.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esami.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to typeset exams with multiple choice, open
questions and many other types of exercise. Both questions and answers
may be randomly distributed within the exam, and the solutions are
typeset automatically. Exercises may contain a wide number of random
parameters and it is possible to do arithmetical operations on them. The
package is localised in Italian, English, French, German, Greek,
Serbian, and Spanish.

