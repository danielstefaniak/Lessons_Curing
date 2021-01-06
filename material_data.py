import numpy as np


def calc_psi(rho_f, rho_m, phi=.6, **kwargs):
    """Calculate the fibre mass ration from fibre and resin density and fibre volume fraction"""
    return rho_f * phi / (rho_f * phi + rho_m * (1 - phi))


def calc_cp_comp(c_f, c_m, rho_f, rho_m, phi=.6, **kwargs):
    """calculate combined heat capacity of composite material with fiber volume content phi"""
    c_comp = (c_f * rho_f * phi + c_m * rho_m * (1 - phi)) / (rho_f * phi + rho_m * (1 - phi))
    return c_comp


def calc_k_comp(k_f_parallel, k_f_perp, k_m, phi=.6, **kwargs):
    """
    calculate thermal diffusivity in and perpendicular to fiber direction of (UD)
    composite material with fiber volume content phi
    """

    k_parallel = k_f_parallel * phi + k_m * (1 - phi)
    k_perp = 1 / (phi / k_f_perp * phi + (1 - phi) / k_m)

    return k_parallel, k_perp


def calc_rho_comp(rho_f, rho_m, phi=.6, **kwargs):
    """calculate density composite material with fiber volume content phi"""
    rho = rho_f * phi + rho_m * (1 - phi)
    return rho


def calc_alpha(k, rho, cp, **kwargs):
    """Calculate thermal diffusivity from thermal conductivity k, density rho and specific heat capacity cp"""
    return k / (rho * cp)


def calc_alpha_comp(k_parallel, k_perp, rho, cp, **kwargs):
    """Calculate thermal diffusivity for composite from thermal conductivity k, density rho and specific heat capacity cp"""
    alpha_parallel = calc_alpha(k_parallel, rho, cp)
    alpha_perp = calc_alpha(k_perp, rho, cp)
    return alpha_parallel, alpha_perp


def rotate_property(p_parallel, p_perp, theta=0):
    return p_parallel * np.cos(theta) ** 2 + p_perp * np.sin(theta) ** 2


def calc_alpha_rotated(alpha_parallel, alpha_perp, theta, deg=True, **kwargs):
    if deg:
        theta *= np.pi / 180
    alpha_x = rotate_property(alpha_parallel, alpha_perp, theta)
    alpha_y = rotate_property(alpha_perp, alpha_parallel, theta)
    return alpha_x, alpha_y


def build_comp_material(material_data, phi=.6, theta=0, deg=True):
    material_data.update(dict(phi=phi))
    if deg:
        material_data.update(dict(theta=theta * np.pi / 180,
                                  theta_deg=theta))
    else:
        material_data.update(dict(theta=theta,
                                  theta_deg=theta * 180 / np.pi))

    rho = calc_rho_comp(**material_data)
    material_data.update(dict(rho=rho))

    psi = calc_psi(**material_data)
    material_data.update(dict(psi=psi))

    cp = calc_cp_comp(**material_data)
    material_data.update(dict(cp=cp))

    k_parallel, k_perp = calc_k_comp(**material_data)
    material_data.update(dict(k_parallel=k_parallel, k_perp=k_perp))

    alpha_parallel, alpha_perp = calc_alpha_comp(**material_data)
    material_data.update(dict(alpha_parallel=alpha_parallel, alpha_perp=alpha_perp))

    alpha_x, alpha_y = calc_alpha_rotated(**material_data, deg=False)
    material_data.update(dict(alpha_x=alpha_x, alpha_y=alpha_y))

    return material_data


def build_comp_material_quick(fibre_material="CF", phi=.6, theta=0, deg=True):
    if fibre_material == "CF":
        reinforcement = CF
    elif fibre_material == "GF":
        reinforcement = GF
    else:
        raise NotImplementedError("Other materials not implemented")
    matrix = EP

    return build_comp_material({**reinforcement, **matrix}, phi=phi, theta=theta, deg=deg)


#### Material data
# disclaimer: only example data. data mixed from different sources.
# many properties highly depending on temperature (and degree of cure)
# [Das Ingenieurwissen - Technische Thermodynamik, S. 71, Tabelle 4-4]
steel = dict(rho=7850,
             cp=465,
             k=50)
steel.update(dict(alpha=calc_alpha(**steel)))
aluminium = dict(rho=2700,
                 cp=888,
                 k=237)
aluminium.update(dict(alpha=calc_alpha(**aluminium)))

# [Schürmann2007] where not indicated otherwise
# Carbon fiber example
CF = dict(k_f_parallel=10,  # ST T800 fibre
          k_f_perp=1.7,     # ST T800 fibre
          rho_f=1700,
          c_f=710)      # [TohoTenaxHTA40]

# Glass fiber example
GF = dict(k_f_parallel=1,
          rho_f=2540,
          c_f=594)      # [Hein2015]
GF.update(dict(k_f_perp=GF.get("k_f_parallel")))    # same value

# Epoxy resin
EP = dict(k_m=.21,      # [Hein2015]
          rho_m=1110,   # [RTM6] uncured
          c_m=1224)     # [Hein2015]



