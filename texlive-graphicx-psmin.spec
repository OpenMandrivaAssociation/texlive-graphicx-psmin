# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/graphicx-psmin
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-graphicx-psmin
Version:	1.1
Release:	6
Summary:	Reduce size of PostScript files by not repeating images
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphicx-psmin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.source.tar.xz
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
%{_texmfdistdir}/tex/latex/graphicx-psmin/graphicx-psmin.sty
%doc %{_texmfdistdir}/doc/latex/graphicx-psmin/README
%doc %{_texmfdistdir}/doc/latex/graphicx-psmin/graphicx-psmin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/graphicx-psmin/graphicx-psmin.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 752388
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718579
- texlive-graphicx-psmin
- texlive-graphicx-psmin
- texlive-graphicx-psmin
- texlive-graphicx-psmin

