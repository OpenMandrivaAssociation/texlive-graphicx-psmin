Name:		texlive-graphicx-psmin
Version:	56931
Release:	1
Summary:	Reduce size of PostScript files by not repeating images
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphicx-psmin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an extension of the standard graphics bundle
and provides a way to include repeated PostScript graphics (ps,
eps) only once in a PostScript document. This provides a way to
get smaller PostScript documents when having, for instance, a
logo on every page. This package only works when post-processed
with dvips, which should at least have version 5.95b. The
difference for a resulting distilled PDF file is minimal (as
Ghostscript and Adobe Distiller only include a single copy of
each graphics file, anyway).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/graphicx-psmin
%doc %{_texmfdistdir}/doc/latex/graphicx-psmin
#- source
%doc %{_texmfdistdir}/source/latex/graphicx-psmin

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
