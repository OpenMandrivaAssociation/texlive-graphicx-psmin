%global tl_name graphicx-psmin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Reduce size of PostScript files by not repeating images
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphicx-psmin
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicx-psmin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is an extension of the standard latex-graphics bundle and
provides a way to include repeated PostScript graphics (ps, eps) only
once in a PostScript document. This leads to smaller PostScript
documents when having, for instance, a logo on every page. The package
only works when post-processed with dvips, which should be version 5.95b
or later. The difference for a resulting distilled PDF file is minimal
(as Ghostscript and Adobe Distiller only include a single copy of each
graphics file, anyway).

