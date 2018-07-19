def monte_2d(f, v, domain, trials):
    """
    Compute area of circle using Monte Carlo sampling
    Parameters
    ----------
    f : function
        User defined function.
    domain : numpy array
        Integration domain.
    v : function
        Integration volume .
    Returns
    -------
    I : float
        Integration result.
    """

    area = np.prod(domain[1] - domain[0])
    matrix = np.sqrt(area) * np.random.rand(trials, 2) + np.min(domain)
    v_eval = v(matrix)
    idx = np.where(v_eval < 1.0)
    points_inside = v_eval[idx]
    k = points_inside.size
    return area * k / trials
