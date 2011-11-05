# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/graphicx-psmin
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-graphicx-psmin
Version:	1.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/graphicx-psmin/graphicx-psmin.sty
%doc %{_texmfdistdir}/doc/latex/graphicx-psmin/README
%doc %{_texmfdistdir}/doc/latex/graphicx-psmin/graphicx-psmin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/graphicx-psmin/graphicx-psmin.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
