Name:		texlive-newfloat
Version:	68434
Release:	1
Summary:	Define new floating environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newfloat
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers the command \DeclareFloatingEnvironment,
which the user may use to define new floating environments
which behave like the LaTeX standard foating environments
figure and table.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/newfloat
%{_texmfdistdir}/tex/latex/newfloat
%doc %{_texmfdistdir}/doc/latex/newfloat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
