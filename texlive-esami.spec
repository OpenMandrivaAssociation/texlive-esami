Name:		texlive-esami
Version:	71883
Release:	1
Summary:	Typeset exams with scrambled questions and answers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/esami
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esami.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esami.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/esami
%doc %{_texmfdistdir}/doc/latex/esami

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
