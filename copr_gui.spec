Name:           copr-gui
Version:        0.1.0
Release:        1%{?dist}
Summary:        GUI for managing COPR instances

License:        GPL-3.0-or-later
URL:            https://github.com/qr243vbi/copr-gui
Source0:        %{url}/archive/refs/tags/%{version}/copr_gui-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros

Requires:       python3-pyqt6
Requires:       python3-copr
Requires:       python3-munch

%description
A Qt-based graphical user interface for managing COPR instances.

%prep
%autosetup -n copr_gui-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files copr_gui copr_gui_source_types

%check
%pyproject_check_import

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/copr-gui

%changelog
* Fri Sep 18 2026 qr243vbi <qr243vbi@atomicmail.io> - 0.1.0-1
- Initial package
