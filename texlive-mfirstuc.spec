Name:		texlive-mfirstuc
Version:	64743
Release:	1
Summary:	Uppercase the first letter of a word
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mfirstuc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfirstuc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfirstuc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfirstuc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands \makefirstuc that uppercases the
first letter in its argument (with a check for a semantic
markup command at the start of the argument), and \xmakefirstuc
which expands the argument before uppercasing. It also provides
\capitalisewords{phrase} which applies \makefirstuc to each
word in the phrase, where the words are separated by regular
spaces. (Exceptions can be made for words that shouldn't be
converted.)

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mfirstuc
%{_texmfdistdir}/tex/latex/mfirstuc
%{_texmfdistdir}/scripts/mfirstuc
%doc %{_texmfdistdir}/doc/latex/mfirstuc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
