project('CLI Project', 'cpp',
  version : '0.1',
  default_options : ['warning_level=2',
                     'cpp_std=c++20',
                     'c_std=c17',
                     'default_library=static'])
                     
std_lib_facilities_dep = dependency('std_lib_facilities', fallback: ['std_lib_facilities', 'std_lib_facilities_dep'])

if host_machine.system() == 'linux'
  compiler_flags = ['-Wconversion', '-fdiagnostics-color=always', '-Werror=return-type']
else
  compiler_flags = ['-Wconversion', '-fdiagnostics-color=always', '-Werror=return-type', '-fcolor-diagnostics', '-fansi-escape-codes']
endif

src = []

exe = executable(
  'program',
  src,
'Dummy.cpp',
'DynamicMemory.cpp',
'Matrix.cpp',
'main.cpp',
  dependencies : [std_lib_facilities_dep],
  cpp_args : compiler_flags
)
