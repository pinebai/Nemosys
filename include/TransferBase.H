#ifndef TRANSFERBASE_H
#define TRANSFERBASE_H

#include "nemosys_export.h"
#include "meshBase.H"


class NEMOSYS_EXPORT TransferBase
{
  // constructors and destructors
  public:
    TransferBase()
        : source(nullptr), target(nullptr),
          srcCellLocator(nullptr), trgCellLocator(nullptr),
          checkQual(false), continuous(false), c2cTrnsDistTol(1.e-6)
    {
      std::cout << "TransferBase constructed" << std::endl;
    }

    virtual ~TransferBase()
    {
      std::cout << "TransferBase destroyed" << std::endl;
    }

  // TransferBase factory method
  public:
    static TransferBase *
    Create(const std::string &method, meshBase *source, meshBase *target);

    static std::unique_ptr<TransferBase>
    CreateUnique(const std::string &method, meshBase *source, meshBase *target)
    {
      return std::unique_ptr<TransferBase>(
          TransferBase::Create(method, source, target));
    }

  // transfer methods
  public:
    // transfer point data with given id from source to target
    virtual int transferPointData(const std::vector<int> &arrayIDs,
                                  const std::vector<std::string> &newnames = std::vector<std::string>()) = 0;
    // transfer cell data with given id from source to target
    virtual int transferCellData(const std::vector<int> &arrayIDs,
                                 const std::vector<std::string> &newnames = std::vector<std::string>()) = 0;
    // transfer all data from source to target
    virtual int
    run(const std::vector<std::string> &newnames = std::vector<std::string>()) = 0;

    // set whether to check transfer quality
    void setCheckQual(bool x) { checkQual = x; }

    void setContBool(bool x) { continuous = x; }

  protected:
    meshBase *source;
    vtkSmartPointer<vtkCellLocator> srcCellLocator; // search structure 
    meshBase *target;
    vtkSmartPointer<vtkCellLocator> trgCellLocator;
    bool checkQual;
    bool continuous; // switch on / off weighted averaging for cell transfer
    double c2cTrnsDistTol;
};

#endif
