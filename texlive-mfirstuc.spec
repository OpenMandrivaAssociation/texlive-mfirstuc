%global tl_name mfirstuc
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.09
Release:	%{tl_revision}.1
Summary:	Uppercase the first letter of a word
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mfirstuc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfirstuc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfirstuc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfirstuc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands \makefirstuc that uppercases the first
letter in its argument (with a check for a semantic markup command at
the start of the argument), and \xmakefirstuc, which expands the
argument before uppercasing. It also provides \capitalisewords{phrase}
which applies \makefirstuc to each word in the phrase, where the words
are separated by regular spaces. (Exceptions can be made for words that
shouldn't be converted.)

