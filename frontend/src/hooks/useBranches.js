import { useCallback, useEffect, useState } from 'react';
import { getBranches } from '../services/branchApi';

export default function useBranches({ activeOnly = false } = {}) {
  const [branches, setBranches] = useState([]);
  const [loading, setLoading] = useState(true);

  const reload = useCallback(async () => {
    try {
      setLoading(true);
      const list = await getBranches({ active: activeOnly });
      setBranches(list);
    } catch {
      setBranches([]);
    } finally {
      setLoading(false);
    }
  }, [activeOnly]);

  useEffect(() => {
    reload();
  }, [reload]);

  return { branches, loading, reload };
}
